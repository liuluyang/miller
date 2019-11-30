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


# ���ű�
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



# 16.#��������department�в����¼
insert into department1 values
(1,'ŷ�²�������������ҵ��'),
(2,'������˹������Դ��'),
(3,'���۲�');



#�����ӱ�employee�в����¼
insert into employee values
(1,'egon',1),
(2,'alex1',2),
(3,'alex2',2),
(4,'alex3',2),
(5,'��̹��',3),
(6,'���ɻ�',3),
(7,'�Ż��',3),
(8,'���ӵ�',3),
(9,'������',3);



# �������
create table press(
id int primary key auto_increment,
name varchar(20)
);

# book ��
create table book(
    id int primary key auto_increment,
    name varchar(20),
    press_id int not null,
    constraint foreign key(press_id) references press(id) on delete cascade on update cascade
);


select book.name from press,book where book.press_id=press.id and press.name="֪ʶ��Ȩû���ó�����";
# "�ѿ�����"

# ���߱�
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
('������ҵ���׳�����'),
('�������ֲ�����������'),
('֪ʶ��Ȩû���ó�����');

insert into book(name,press_id) values
('������',1),
('�����澭',2),
('�����׹�צ',2),
('���¾Ž�',3),
('����ʮ����',2),
('��������',3);


insert into author(name) values('egon'),('alex'),('yuanhao'),('wpq');

# 22.egon:   1
# 23.������       1
# 24.�����澭       2
# 25.�����׹�צ     3
# 26.���¾Ž�       4
# 27.����ʮ����     5
# 28.��������       6
# 29.alex:  2
# 30.������
# 31.��������
# 32.yuanhao:  3
# 33.���¾Ž�
# 34.����ʮ����
# 35.��������
# 36.wpq:  4
# 37.������

insert into book2author (author_id, book_id) VALUES (1,1), (1, 2),(1,3), (1, 4), (1,5), (1, 6),
                                                    (2, 1),(2, 6),
                                                    (3, 4),(3,5),(3,6),
                                                    (4,1);
