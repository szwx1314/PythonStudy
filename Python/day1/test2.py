#
# while True:
#     num = int(input("输入："))
#     if num >10:
#         print(num)
#         break
#     else:
#         print("小于10")

#
# dic ={'name':'杨士永','age':'28'}
# ret = dic.setdefault('sex','man')
# print(ret)
# print(dic)
# print(dic['age'])
# print(dic.keys())
# a,b,c=list(dic.keys())
# a0,b0,c0 =list(dic.values())
# print(list(dic.items()))
# print(a)
# print(b)
# print(c)
# print(a0)
# print(b0)
# print(c0)


dic1 ={'name':'杨士永','sex':'man'}
dic2 ={'name':'董瑶瑶','sex':'women','age':'28'}
print(dic1)
dic1.update(dic2)
print(dic1)
ret = dic1.pop('name')
print(ret)