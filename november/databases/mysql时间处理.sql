
# 返回 日期的 时间戳格式
select curtime();  # 19:24:22
select curdate();  # 2019-11-03
select now(); # 2019-11-03 19:24:22


select current_timestamp(); # 2019-11-03 19:24:22  # 当前系统时间,不怎么使用因为涉及到时区,(这个会根据时区的变化而变化)
set time_zone = "+9:00";  # 设置时区后 得到的时间将不再一样。


select unix_timestamp(curtime());
select unix_timestamp(curtime());
select unix_timestamp(current_date());

select from_unixtime(unix_timestamp(curtime()));  # 将时间戳格式的时间, 转换成格式化时间. 可指定格式

select week(now());  # 返回一年当中的第几个星期
select year(now());  # 返回年  2019
select date (now());  # 返回日期  2019-11-03
select hour(now());  # 返回小时  5
select minute(now());  # 返回分钟 59


# 演示 如何将时间 以每半个小时 一分组，并返回这个每个半小时之内有几条数据插入。
create table time_test(id int auto_increment primary key , sub_time datetime);

insert into time_test(sub_time)
values
       ("2019-11-03 9:30:29"),
       ("2019-11-03 9:59:29"),
       ("2019-11-03 11:22:29"),
       ("2019-11-03 11:08:29"),
       ("2019-11-03 13:30:29"),
       ("2019-11-03 13:59:29"),
       ("2019-11-03 22:10:29"),
       ("2019-11-03 22:22:29"),
       ("2019-11-03 22:30:29"),
       ("2019-11-03 22:50:29");

select count(incount), a.dataStartTime from
(select id as incount, date_format(concat(date(sub_time)," ", hour(sub_time),":",floor(minute(sub_time)/30)*30), "%Y-%m-%d %H:%i") as dataStartTime from time_test) a
group by (date_format(dataStartTime, "%Y-%m-%d %H:%i"))

# 将每个时间的分钟取出, 与30进行地板除。得到的不是0 就是1。 然后得到一张虚拟表, 以这张虚拟表中的时间为分组依据进行分组然后统计每个半小时内出现的插入的记录次数。

# create table time_test11(sub_time time);
# insert into time_test11 values (curtime());
# select unix_timestamp(sub_time) from time_test11;
# insert into time_test11 values ("17:22:29");
# select unix_timestamp(sub_time) from time_test11;


