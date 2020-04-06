import configparser
'''
configparser-INI配置文件解析工具
官网：
    https://docs.python.org/zh-cn/3/library/configparser.html
'''

class ReadConfig(object):
    def __init__(self,filename):
        #设置配置文件路径
        self.filepath = "../newbie/" + filename
    def read_mysql(self):
        config = configparser.ConfigParser()
        config.read(self.filepath,encoding="utf-8")
        db_ip = config["mysql"]["db_ip"]
        username = config.get("mysql","username")
        password = config.get("mysql","password")
        db_name = config.get("mysql","db_name")

        print("config.ini文件的数据:db_ip:{0},username:{1},password:{2},db_name:{3}".format(db_ip,username,password,db_name))
        return db_ip,username,password,db_name

    def read_config(self):
        #配置文件读入
        config = configparser.ConfigParser()
        config.read(self.filepath,encoding="utf-8-sig")

        #读取DB部分
        db_ip = config.get("db","ip")
        db_port = config.getint("db", "port")
        db_user = config.get("db", "user")
        db_password = config.get("db", "password")
        db_database = config.get("db", "database")
        print(db_ip,db_port,db_user,db_password,db_database)

        #另一种读取方式
        db_ip2 = config["db"]["ip"]
        print("新方法读取IP为：%s"%(db_ip2))

        #获取所有节点返回一个列表
        ret = config.sections()
        print("所有节点为：%s"%(ret))

        #获取节点下键值
        ret1 = config.items("db")
        print("db下的键值是：%s"%(ret1))

        #获取某个节点下的键
        ret2 = config.options("db")
        print("db节点下的键为：%s"%(ret2))

        '''
        #获取指定节点下的key的值，默认为str类型
        v = config.get('node1', 'k1')
        v = config.getint('node1', 'k1')
        v = config.getfloat('node1', 'k1')
        v = config.getboolean('node1', 'k1')
        '''

        '''
        #检查、添加、删除节点和节点下的值
        has_sec = config.has_section('node1')  # 检查该[节点]是否存在
        has_opt = config.has_option('node1', 'k1')  # 检查该[节点]下的 'key' 是否存在
        config.add_section('node2')  # 添加[节点]

        config.set('node2', 'k1', '123')  # 添加[节点]下的 key=value
        config.remove_section('node2')  # 移除节点
        config.remove_option('node2', 'k2')  # 移除[节点]下的 'key'
        '''


        # config.add_section('node2')  # 添加[节点]
        # config.set('node2', 'k1', '123')  # 添加[节点]下的 key=value
        ret3 = config.get("node2","k1")
        print("添加的node2的k1值为：%s"%(ret3))

        # 修改完记得保存
        with open(self.filepath,"w") as f:
            config.write(f)



if __name__ == "__main__":
    ReadConfig("config.ini").read_mysql()