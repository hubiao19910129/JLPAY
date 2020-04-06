print("{:*^40}".format("while-continue-else语句"))
#while--continue--else
i = 1
while i < 10:
    i += 1
    if i%2 == 0:
        continue
    print(i)
else:
    print("{} is not less 10".format(i))

print("{:*^40}".format("while-break语句"))
#while--break
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

print("{:*^40}".format("for语句"))
#for
fruits = ["apple","banana","mango"]
# print(len(fruits)) #3
for index in range(len(fruits)):
    # print(index) #0、1、2
    print(fruits[index])
print("Good Bey！")

print("{:*^30}".format("for语句求10~19中的质数"))
for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print("{0} = {1} * {2:.0f} ".format(num,i,j))
            break
    else:
        print("{} 是质数".format(num))