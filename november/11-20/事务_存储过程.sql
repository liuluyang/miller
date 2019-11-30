# delimiter //
# create procedure test1()
# begin
#     begin
#         declare exit handler for sqlwarning,sqlexception, not found
#             start transaction ;
#                 insert into balance (id, name, balance) values ("alex", 500);
#                 insert into balance (name, balance) values ("alex", 500);
#                 insert into balance (name, balance) values ("alex", 500);
#             commit ;
#     end ;
# end //
# delimiter ;


# delimiter //
# create procedure test23()
# begin
#     declare exit handler for sqlexception
#         begin
#             set @p_return_code = 1;
#             rollback;
#         end;
#
#     declare exit handler for sqlwarning
#         begin
#             set @p_return_code = 2;
#             rollback;
#         end;
#
#     start transaction ;
#     delete from tb1;
#     insert into balance (name, balance) values ("alex", 500);
#     insert into balance (name, balance) values ("alex", 500);
#     commit ;
#
#     set @p_return_code = 0;
# end //
# delimiter ;


delimiter //
create function test(a int)
returns int
begin
        return a*2;
end //
delimiter ;


