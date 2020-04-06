
'''
    目标：
        1、搜索测试套件
        2、运行测试套件、并生成测试报告
'''
#导包 unittest HTMLTestRunner time
import unittest
import os
import time
# from tools.HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner import  HTMLTestRunner

class RunTest(object):
    def __init__(self):
        pass

    def run_test(self):
        # discover（路径,文件名），递归找到指定目录下的测试模块
        test_dir = "./cass"
        test_list = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

        #report_path 存放日志的路径
        now_time = time.strftime("%Y_%m_%d %H_%M_%S")
        report_dir = "./report"
        report_path = os.path.join(report_dir,"{}.html".format(now_time)).encode("utf-8")

        try:
            with open(report_path,"wb") as f:
                HTMLTestRunner(stream=f,title="彪哥威武",description="测试环境 WIN7").run(test_list)
        except Exception as e:
            print("执行run_case报错" + e)
        else:
            f.close()
            print("\n succesful to run run_case!")
            #画pikachu
            # from newbie import draw_pikachu
            # draw_pikachu.main()
if __name__ == "__main__":
    RunTest().run_test()


