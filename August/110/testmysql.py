#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql, datetime
from collections import defaultdict


def get_mysql_data(host, user, passwd, db_name, table_name, *args):
    config_dict = defaultdict(list)
    conn = pymysql.connect(host=host, user=user, passwd=passwd, database=db_name, charset="utf8")
    cursor = conn.cursor()
    query_columns = ','.join(args)
    sql = "select %s  from %s where id >= 2000 and id <=2500 " % (query_columns, table_name)
    cursor.execute(sql)
    for value in cursor.fetchall():
        # for index, i in enumerate(args):
        #     if type(value[index]) == datetime.date:
        #         # 不同格式 则做不同处理
        #         row = value[index].strftime('%Y-%m-%d')
        #     else:
        #         row = value[index]
        #     config_dict[i].append(row)
        print(value)
        '''
        tmp_dict = dict(zip([i], [row]))
        server_list.append(tmp_dict)
        '''


# return config_dict


# def combine_data(admin_config_dict, bastion_config_dict):
#     for item in admin_config_dict.values():
#         for k, item_list in bastion_config_dict.items():
#             if item not in item_list:
#                 print(item)


def main():
    column_map = {'onlinedate': 'opentime', 'id': 'serverid', 'name': 'servername'}

    admin_config_dict = get_mysql_data('127.0.0.1', 'root', '123456', 'game_admin_hw', 't_server_config', 'onlinedate',
                                       'id', 'name')

    bastion_config_dict = get_mysql_data('127.0.0.1', 'root', '123456', 'bastion', 'websshapp_serverlist', 'opentime',
                                         'serverid', 'servername')

    # combine_data(admin_config_dict, bastion_config_dict)


if __name__ == '__main__':
    main()
