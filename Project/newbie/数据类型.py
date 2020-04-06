# -*- coding: UTF-8 -*-
#!/usr/bin/python
print("{:*^30}".format("number数据类型"))
'''
python 中支持4中：
    int      #通常被称为是整型或整数，是正或负整数，不带小数点;
    long     #无限大小的整数，整数最后是一个大写或小写的L;
    floate   #浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）;
    complex  #复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型;
'''
#类型转换：
x = "66"
y = 2
print(int(x ),type(int(x )))        #将x转换为一个整数
print(float(x),type(float(x)))      #将x转换为浮点型
print(complex(x),type(complex(x)))  #将x转换为复数
print(str(y),type(str(y)))          #将X转换成字符串
print(repr(x),type(repr(x)))        #将x转换成表达式字符串
print(eval(x),type(eval(x)))        #去掉字符串外衣，展示里面的类型
print(tuple(x),type(tuple(x)))      #将x转换成元组
print(list(x),type(list(x)))        #将x转换成字典
print(chr(y),type(chr(y)))          #将整数转换成一个字符

print("{:*^30}".format("math模块"))
import math
print(abs(-10))          #取绝对值
print(math.floor(4.65))  #返回数字的下舍整数
print(math.ceil(4.65))   #返回数字的上舍整数

print("{:*^30}".format("operator模块"))
import operator
print(operator.eq(10,20)) #等于True,不等于False
print(operator.ne(10,20)) #不等于
print(operator.lt(10,20)) #小于
print(operator.le(10,20)) #小于等于
print(operator.gt(10,20)) #大于
print(operator.ge(10,20)) #大于等于

print("contains：",operator.contains("abcde","abcd"))   #contains(a,b),如果b in a 则True
print("concat:",operator.concat("ab","cd"))             #字符串拼接
print("is:",operator.is_("ab","ab"))                    #识别字符串

list2 = {"a":"b","k":"d"}
operator.setitem(list2,"k","v")   #索引赋值
print("索引赋值obj[k]=v：{}".format(list2))

operator.delitem(list2,"k")       #删除赋值
print("删除赋值 obj[k]:{}".format(list2))

operator.getitem(list2,"a")       #删除赋值
print("索引 obj[a]:{}".format(operator.getitem(list2,"a") ))
