import os

class OsPath(object):
    def __init__(self,filePath):
        self.filePath = filePath
        pass

    def judge_dir(self):
        if os.path.isdir(path=self.filePath):
            return self.filePath
        else:
            pass

    def judge_file(self):
        if os.path.isfile(path=self.filePath):
            return self.filePath
        else:
            pass

    def get_localPath(self):
        #获取当前文件的绝对路径，带有文件名
        file = os.path.realpath(__file__) #D:\TOOLS\JLPAY\JLPAY\Project\zero\os_path.py
        # file = __file__
        print("当前文件信息为：%s"%(file))

        #获取当前文件的绝对路径，去掉文件名
        filePath = os.path.dirname(file)
        print("当前文件的路径为：%s"%(filePath))

        #获取当前文件名
        fileName = os.path.basename(file)
        print("当前文件的文件名为:%s"%(fileName))

        #分隔当前路径 和 文件名
        fileNamePath = os.path.split(file)
        print("当前文件的路径为%s、文件名为:%s"%(fileNamePath))

        #将目录和文件名合并
        #os.path.join(path1[, path2[, ...]])
        fileSum = os.path.join(filePath,fileName).encode("utf-8")
        print("合并目录、文件名为：%s"%(fileSum.decode("utf-8")))

        #方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        list = os.listdir(filePath)
        print("目录%s下的文件有：%s"%(filePath,list))



if __name__ == "__main__":
    OsPath(filePath="abc").get_localPath()