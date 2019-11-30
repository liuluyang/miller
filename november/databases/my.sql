# IF CASE
# 准备表
create table salary
(
    id   int primary key auto_increment,
    name varchar(10),
    sal  float(10, 2)
);

insert into salary(id, name, sal)
VALUES (1, "miller", 1000),
       (2, "liusir", 2000),
       (3, "alex", 3000),
       (4, "egon", 4000);


# select name, case sal when 4000 then "high" end from salary;
# 查询工资情况  并返回结果
select name,
       case
           when (sal>=4000) then "high"
           when (sal>=2000) then "mid"
           else "low"
           end sal from salary;

# ###############################################################################
# 触发器
create table cmd
(
    id       int primary key auto_increment,
    name     char(10),
    cmd      char(10),
    sub_time datetime,
    success  enum ("yes", "no")
);


create table error_log
(
    id       int primary key auto_increment,
    err_cmd  char(10),
    err_time datetime
);

# 在向cmd表 插入数据后, 触发触发器 并且根据 success的执行成功与否, 进而想 error_log 表中插入数据。
delimiter //
create trigger ins_cmd_aft
    after insert
    on cmd
    for each row
BEGIN
    if NEW.success = "no" then
        insert into error_log(err_cmd, err_time) values (new.cmd, now());
    end if;
end //
delimiter ;

insert into cmd(name, cmd, sub_time, success)
VALUES ("miller", "dir", now(), "yes"),
       ("liusir", "cd", now(), "no"),
       ("alex", "pwd", now(), "no");

# 再来看一看在 before insert, after insert,  before update, after update, 在进行插入记录, 修改时触发情况

drop trigger ins_cmd_aft;  # 先将前面的那个触发器删掉。

create table tri_demo(id int auto_increment primary key , note varchar(20));

delimiter //
create trigger ins_cmd_bef before insert on cmd for each row
    begin
        insert into tri_demo(note) values ("befor insert");
    end //

create trigger ins_cmd_aft after insert on cmd for each row
    begin
        insert into tri_demo(note) values ("after insert");
    end //

create trigger upd_cmd_bef before update on cmd for each row
    begin
        insert into tri_demo(note) values ("befor update");
    end //

create trigger upd_cmd_aft after update on cmd for each row
    begin
        insert into tri_demo(note) values ("after update");
    end //
delimiter ;

# 在插入记录已经存在的情况下
# ON DUPLICATE KEY UPDATE 这是一个特别的语句, 作用就是用于当要插入的新数据, 和旧数据有冲突的时候
# 可以自动的选择 更新这条数据, 而不是报错。
# 这个东西还是非常强的, 比如你插入多条数据的时候,它会自动的判断当前这条数据是否是 有冲突的,
# 有冲突就执行更新操作，没有的话就执行插入操作。(是否有冲突是根据主键确定的) very good!

insert into cmd(id, name, cmd, sub_time, success)
values (1, "alex", "ls", now(), "yes")
on duplicate KEY UPDATE name=values(name),
                        cmd=values(cmd),
                        sub_time=values(sub_time),
                        success=values(success);

# 在看看 插入新记录的情况!
truncate table tri_demo;  # 清空表记录 自动增长id 从1 开始
delete from tri_demo;  # 删除表记录 自动增长id 从上一次最大id开始。

insert into cmd(id, name, cmd, sub_time, success)
values (4, "alex", "ls", now(), "yes");

# ###############################################################################
# 过程和函数
# 传入的参数分 IN OUT INOUT
# IN 只是传入参数, OUT 用于返回参数
create table test1(name varchar(10));

# 可以有写数据的 语句
delimiter //
create procedure ins_test1(in name varchar(10))
modifies sql data
BEGIN
    insert into test1 values (name);
end//
delimiter ;

# 查数据

delimiter //
create procedure sel_test1(in name varchar(10), out res int)
reads sql data
BEGIN
    select * from test1 where test1.name=name;
    select FOUND_ROWS() into res;
end //
delimiter ;

# set @a = 0;  # out 传入参数的初始值
# call sel_test1("alex", @a)  # 传入

# 函数 要记住函数只能用于 sql语句当中。
delimiter //
create function func(a int, b int)
returns int # 需要提前说明 要返回的是什么东西。
BEGIN
    return a + b;
end //
delimiter ;


# #############################################################################
# 事务控制 和 锁定语句  （事务超级重要, 原子操作）
# 事务 简单理解就是 你要向另一个人转账, 你的账户减少前, 他的账户增加。 这两个操作要么同时成功
# 要么同事失败。  一种原子行操作。

# MySql 支持对MyISAM 和 MEMORY 存储引擎的表进行 表计锁定。对BDB存储引擎进行页及锁定

# 准备表
create table balance(id int auto_increment primary key, name varchar(10), balance decimal(8,2));

insert into balance(name, balance) values ("black_gril", 5000),("liusir", 6000),("xiaobai",10000);

start transaction ;
        update balance set balance=5900 where name="black_gril";
        update balance set balance=5000 where name="liusir";
        update balance set balance=10100 where name="xiao";
rollback ;
commit ;

# 再一次测试,

# 创建表
create table actor(id int auto_increment primary key , name varchar(10));
# 开始一个新的事务
start transaction ;
insert into actor (id, name) values (1, "miller1");
# 不执行commit查看
select * from actor where id=1;
# 执行commit 再看。
commit ;
select * from actor where id=1;

# 这样不开启新事务, 执行插入。 是默认进行提交的。
insert into actor (id, name) values (2, "miller2");
select * from actor where id in (1, 2);

# 再开始一个新事务
start transaction;
insert into actor (id, name) values (3, "miller3");

# 使用 commit and chain 进行提交；
commit and chain ;
# 这里会自动的 再去开启一个新的事务。
insert into actor (id, name) values (4, "miller4");
select * from actor where name="miller4";  # 你是看不到这条数据的。
commit ; # 提交你就看到了


# 注意所有的 DDL语句. 数据库定义语句 是不能进行回滚操作的。所以你别这么用了就。


# 权限的例子
grant select on *.* to miller@localhost; # 创建用户 miller@localhost 并赋予数据库上的所有表的 select 权限
revoke select on *.* from miller@localhost;  # 收回权限
grant select on test1.* to miller@localhost;  # 给与只对test1 这个数据库有 select 权限。

grant all on *.* to liusir@localhost; # 给予 liusir@localhost 所有的权限, 但是唯独授权的权限是不给的。

grant all privileges on *.* to liusir@localhost with grant option ;  # 给予授权的权限。

grant all privileges on *.* to liusir@localhost identified by "123" with grant option; # 再加个密码


select * from mysql.user where user="liusir" and host="localhost"\G;


# 创建新用户 alex 只给与 select update insert delete 对test1表的权限 密码为123 可以从任何ip登陆。

create database test1;

grant select,update,insert,delete on "test1.*" to "alex"@"%" identified by "123";

# 授权super, process, file权限给 xxx。
grant super, process, file on *.* to "xxx"@"%";
# 这几个权限都是管理权限, 是不能指定某一个数据库的, 所以必须要有 *.*


grant usage on *.* to "priv4"@"localhost";  # usage 只是授予登陆权限, 其他一概没有。(这有个鸡的用)


