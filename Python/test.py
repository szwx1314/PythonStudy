# -*- coding:utf-8 -*-
# Author:YSY


print("这是第一个python程序")

name ="杨士永"

name2 = name
print(name,name2)
'''
print("这是多行注释")
'''
name = "董瑶瑶"

print(name,name2)

msg ='''
name = "这是没什么卵用的赋值"
print("这是打印多行的方式")
'''

print(msg)


inputstr = input("请输入一句话")

print(inputstr)



list = [1,2,3,4,5,6]
list1 = set(list)

print(list1.pop(),list1)

print(list1.discard(1231231))