create table department
(
    id   int primary key auto_increment, # not null unique
    name varchar(20),
    pwd  varchar(16)
);

create table server
(
    ip varchar(15),
    port char(5),
    service_name varchar(10) not null,
    primary key (ip, port)
);


# 部门表
create table department1(
    id int primary key auto_increment,
    name varchar(20) not null
)engine=innodb;

create table employee(
    id int primary key auto_increment,
    name varchar(20) not null,
    dpt_id int,
    foreign key(dpt_id) references department1(id)
        #[constraint] [name] foreign key (column_name) references tb_name(tb_name.column_name)
    on DELETE CASCADE on UPDATE CASCADE
)engine=innodb;



# 16.#先往父表department中插入记录
insert into department1 values
(1,'欧德博爱技术有限事业部'),
(2,'艾利克斯人力资源部'),
(3,'销售部');



#再往子表employee中插入记录
insert into employee values
(1,'egon',1),
(2,'alex1',2),
(3,'alex2',2),
(4,'alex3',2),
(5,'李坦克',3),
(6,'刘飞机',3),
(7,'张火箭',3),
(8,'林子弹',3),
(9,'加特林',3);



# 出版社表
create table press(
id int primary key auto_increment,
name varchar(20)
);

# book 表
create table book(
    id int primary key auto_increment,
    name varchar(20),
    press_id int not null,
    constraint foreign key(press_id) references press(id) on delete cascade on update cascade
);


select book.name from press,book where book.press_id=press.id and press.name="知识产权没有用出版社";
# "笛卡尔积"

# 作者表
create table author(
    id int primary key auto_increment,
    name varchar(20)
);

create table book2author(
    id int not null unique auto_increment,
    author_id int not null,
    book_id int not null,
    constraint fk_author foreign key (author_id) references author(id) on delete cascade on update cascade,
    constraint fk_book foreign key (book_id) references book(id) on delete cascade on UPDATE cascade,
    primary key (author_id, book_id)
);



insert into press(name) values
('北京工业地雷出版社'),
('人民音乐不好听出版社'),
('知识产权没有用出版社');

insert into book(name,press_id) values
('九阳神功',1),
('九阴真经',2),
('九阴白骨爪',2),
('独孤九剑',3),
('降龙十巴掌',2),
('葵花宝典',3);


insert into author(name) values('egon'),('alex'),('yuanhao'),('wpq');

# 22.egon:   1
# 23.九阳神功       1
# 24.九阴真经       2
# 25.九阴白骨爪     3
# 26.独孤九剑       4
# 27.降龙十巴掌     5
# 28.葵花宝典       6
# 29.alex:  2
# 30.九阳神功
# 31.葵花宝典
# 32.yuanhao:  3
# 33.独孤九剑
# 34.降龙十巴掌
# 35.葵花宝典
# 36.wpq:  4
# 37.九阳神功

insert into book2author (author_id, book_id) VALUES (1,1), (1, 2),(1,3), (1, 4), (1,5), (1, 6),
                                                    (2, 1),(2, 6),
                                                    (3, 4),(3,5),(3,6),
                                                    (4,1);
