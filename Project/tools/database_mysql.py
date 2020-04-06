#!/usr/bin/python
# -*- coding: UTF-8 -*-

#python3不支持MYSQLdb,所以用pymysql
import pymysql

#建立连接
connection = pymysql.connect("172.20.5.69",     #IP
                             "test",            #user_name
                             "111111",          #password
                             "app_release",     #db_name,通过select database()查询数据库名
                             charset = "utf8"   #字符串连接类型
                             )
print("{:*^50}".format("Congratulation connect MySql is successful !"))

#获取游标对象
cursor = connection.cursor()

#执行的SQL语句
sql = "select *  from gl_app_ios_release_info where commit_id='75a4059c4d9dc03c8929684b2f5a4d4a2bab29e8'"
cursor.execute(sql)
#获取执行结果并断言
result = cursor.fetchone()
print("获取的结果为：{}".format(result))

#结果断言
assert result[-1] == "张世民"

#关闭游标
cursor.close()
#关闭连接
connection.close()




'''
--IOS--
select *  from gl_app_ios_release_info where commit_id='75a4059c4d9dc03c8929684b2f5a4d4a2bab29e8';
--Android--
select *  from gl_app_android_release_info where commit_id='69d86aa2cefb0a52911ffdba2987881613113655';
'''