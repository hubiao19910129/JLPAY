# -*- coding: UTF-8 -*-
import pymysql
import unittest
from newbie.read_config import ReadConfig
from tools.read_mysql import ReadMysql
from parameterized import parameterized
from data.mysql_data import *

def get_config_data():
    data = ReadConfig("config.ini").read_mysql()
    # print("data的值为：{0},data的类型为：{1}".format(data, type(data)))
    arr = []
    arr.append(data)
    return arr


class TestMysql(unittest.TestCase):
    @parameterized.expand(get_config_data())
    def test_mysql(self,db_ip,username,password,db_name):
        # 从mysql_data中获取数据
        sql =eval("sql")
        result = ReadMysql().get_sql_one(sql=sql,db_ip=db_ip,username=username,password=password,db_name=db_name)
        self.assertEqual(result[-1],"张世民")
        self.assertEqual(result[0], 285)

if __name__ == '__main__':
    unittest.main()

