
import os
class FileRedact(object):
    def __init__(self,fileName):
        filePath = os.getcwd()
        print("当前路径为：%s"%(filePath))
        self.filename = os.path.join(filePath,fileName).encode("utf-8")
        print(self.filename)

    def file_read(self):
        with open(self.filename,"r+") as f:
            #从文件的开头开始读，读取10个字节
            str = f.read(10)
            #读取所有
            str1 = f.read()
            #查询文件最好字节的当前位置
            position = f.tell()
            #定位指针
            position = f.seek(0,0)
            '''
            seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
            如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为 参考位置
            '''
        f.close()



    def file_write(self):
        print("*************")
        with open(self.filename,"w") as f:
            f.write("www.runoob.com!\nVery good site!\n")
        f.close()

    def file_repalce(self):
        str = "this is string example....wow!!! this is really string"
        #将is替换成was
        print(str.replace("is", "was"))
        #将is替换成was,替换3次
        print(str.replace("is", "was", 3))

if __name__ == "__main__":
    FileRedact("hubiao").file_write()