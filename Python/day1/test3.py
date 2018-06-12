# f= open('text','r',encoding='utf-8')
# data = f.read(1)
# print(data)
# f.close()


# f= open('text','r',encoding='utf-8')
# date2 =f.readlines()
# # date = f.read()
# print(date2)
# print("--------------")
# print(date)

# print(f.read(1))
# print(f.tell())
# f.seek(0)
# print(f.tell())
#
# f=open('text2.txt','w')
#
# f.write('sadasdasdasdasdsadsadsadsa')
# f.truncate(1)
# f.flush()

# f=open('text','r',encoding='utf8')
# print(f.readline())
# print(f.readline())
# print(f.readline())

# a='he is happy \n yes'
# b=repr('he is happy \n yes')
# print(a)
# print(b)

# s=[1,2,3,4,5,6,7,8,9,10]
#
# print(s[2:5])

f= open('text','w',encoding='utf8')
a = f.write('这是测试文本')
f.flush()
f.close()
print(a)
