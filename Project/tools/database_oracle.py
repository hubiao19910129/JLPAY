# -*- coding: utf-8 -*-
import cx_Oracle

#获取连接对象
# connection = cx_Oracle.connect("username/password@host:port/service_name")
# connection = cx_Oracle.connect("agent_user2/123456@172.20.6.22:1521/mpos")

class TestDataBaseOracle(object):

    def __init__(self,database,sql):
        self.database = database
        self.sql = sql

    def test_database_oracle(self):

        try:
            connection = cx_Oracle.connect(self.database)
            print("{:*^50}".format("congratulation connect Oracle is successful !"))
        except Exception as e:
            print(e)
            raise Exception("数据库连接失败，数据库信息：{}".format(self.database))
        else:
            #获取游标对象
            cursor = connection.cursor()
            #执行SQL
            cursor.execute(self.sql)
            #获取查询结果
            result = cursor.fetchall()
            print(result)
        finally:
            #关闭游标对象
            cursor.close()
            #关闭连接对象
            connection.close()

if __name__ == "__main__":
    db = "agent_user2/123456@172.20.6.22:1521/mpos"
    sql = "select * from t_profit_amount where user_id = 50263545"
    TestDataBaseOracle(database=db,sql=sql).test_database_oracle()


