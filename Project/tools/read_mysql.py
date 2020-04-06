# -*- coding: UTF-8 -*-

import pymysql

class ReadMysql:
    #定义连接对象 类方法
    connection = None
    #获取对象连接方法封装
    def get_connection(self,db_ip,username,password,db_name):
        if self.connection is None:
            self.connection = pymysql.connect(db_ip,
                                              username,
                                              password,
                                              db_name,
                                              charset = "utf8")
        #返回连接对象
        return self.connection

    #获取游标对象方法封装
    def get_cursor(self,db_ip,username,password,db_name):
        cursor = self.get_connection(db_ip,username,password,db_name).cursor()
        return cursor

    #关闭游标对象方法封装
    def close_cursor(self,cursor):
        #如果cursor为空关闭会报错！
        if cursor:
            cursor.close()

    #关闭连接对象方法封装
    def close_connection(self):
        #如果connection为空，关闭会报错
        if self.connection:
            self.connection.close()
            #注意：关闭连接对象后，对象还在内存中，需要手动设置为None
            self.connection = None

    #主要 执行的方法 ->外界调用来完成此次操作
    def get_sql_one(self,sql,db_ip,username,password,db_name):
        #定义游标对象及数据变量
        cursor = None
        data = None

        try:
            #获取游标对象
            cursor = self.get_cursor(db_ip,username,password,db_name)
            #调用执行方法
            cursor.execute(sql)
            #获取结果
            data = cursor.fetchone()
        except Exception as e:
            print("get_sql_one is error",e)
        finally:
            #关闭游标对象
            self.close_cursor(cursor)
            #关闭连接对象
            self.close_connection()
            #返回结果
            print(data)
            return data


if __name__ == '__main__':
    db_ip    ="172.20.5.69"
    username ="test"
    password ="111111"
    db_name  ="app_release"
    sql      = "select *  from gl_app_ios_release_info where commit_id='75a4059c4d9dc03c8929684b2f5a4d4a2bab29e8'"
    # ReadMysql().get_sql_one(sql,db_ip,username,password,db_name)
    ReadMysql().get_sql_one(sql=sql, db_ip=db_ip, username=username, password=password, db_name=db_name)