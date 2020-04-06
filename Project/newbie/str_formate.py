'''
作用：
    格式化字符串的函数 str.format()
    基本语法是通过 {} 和 : 来代替以前的 %

'''
# 1、format 函数可以接受不限个参数，位置可以不按顺序
str1 = "{} *** {}".format("hello","word")     #hello *** word
str2 = "{1} *** {0}".format("hello","word")   #word *** hello
str3 = "{0} *{1}* {0}".format("hello","word") #hello *word* hello
print('''
str1的值为：{0}
str2的值为：{1}
str3的值为：{2}
'''.format(str1,str2,str3))

# 2、也可以设置参数
str4 = "网站名称：{name},网站路径：{url}".format(name = "helloworld",url = "www.helloworld.com")
print("str4的值为：{}".format(str4))

# 3、通过字典设置参数
dict1 = {"name":"helloworld","url":"www.helloworld.com"}
str5 = "网站名称：{name},网站路径:{url}".format(**dict1)
print("str5的值为：{}".format(str5))

# 4、通过元组设置参数,{0}是必须的
list1 = ["hello world","www.hello world"]
str6 = "网站名称：{0[0]},网站路径:{0[1]}".format(list1)
print("str6的值为：{}".format(str6))

# 5、也可以向str.formate()传入对象
class MyValue(object):
    def __init__(self,value):
        self.value = value
my_value = MyValue(6)
str7 = "{0.value}".format(my_value)
print("str7的值为：{}".format(str7))

# 6、str.format() 格式化数字的多种方法
str8 = "{:.2f}".format(3.141592653)  #保留两位小数
print("str8的值为：{}".format(str8),type(str8))
print("{:+.2f}".format(3.141592653))   #保留两位小数，前面带符号
print("{:+.2f}".format(-3.141592653))  #保留两位小数，前面带符号
print("{:+.0f}".format(-3.141592653))  #不带小数，前面带符号

print("**********")
print("{:>10}".format(66))  #右对齐，宽度为10
print("{:<10}".format(66))  #左对齐，宽度为10
print("{:^10}".format(66))  #中间对齐，宽度为10

print("{:*>10}".format(66))  #右对齐，宽度为10，用*填补空缺
print("{:*<10}".format(66))  #左对齐，宽度为10，用*填补空缺
print("{:*^10}".format(66))  #中间对齐，宽度为10，用*填补空缺

print("{:,}".format(10000000)) #以","号分隔数字格式

print("{:.0%}".format(0.25)) #百分比格式，取整25%
print("{:.2%}".format(0.25)) #百分比格式，取两位小数25.00%

print("{:x}".format(11))  #16进制
print("{:d}".format(11))  #10进制
print("{:o}".format(11))  #8进制
print("{:b}".format(11))  #2进制


