#http://www.cnblogs.com/alex3714/articles/5717620.html

s=[1,'杨士永','董瑶瑶']
s2=s.copy()
print(s2)

# 浅拷贝=只拷贝第一层
# 深拷贝=克隆另一份

#浅拷贝
s=[[10000,19999],'杨士永','董瑶瑶']
s1 = s.copy()
s1[0][1] -=1999
print(s)
print(s1)

#深拷贝
import copy #需要引入新的类

s=[[10000,19999],'杨士永','董瑶瑶']
s2=copy.deepcopy(s)
s2[0][1]-=1999
print(s)
print(s2)

# 创建列表
a=[1,2,3]
b=list([4,5,6]) #关键字创建
print(a,type(a))
print(b,type(b))

#创建元组
a0=(1,3,5)
b0=tuple([7,8,9])
print(a0)
print(b0)

#集合（set）

sets=set('alex')
print(sets)

sets2= set(['alex','name','a','a','NAME'])
print(sets2)
print(type(sets2))
print(list(sets2),type(list(sets2))) #set转成list

#set的性质：无序的;不可重复的
#集合的分类：可变集合（set），不可变集合（frozenset）
s001= set('yang')
s002=frozenset('yang')
print(s001,type(s001))
print(s002,type(s002))

#set更新

s003=set(['yang'])
s003.add('dong')

print(s003)
s003.update('yangmh')
print(s003)
s003.update(['yangminghan','yangmh'])
print(s003)

s003.remove('yangminghan')
print(s003)

s003.clear() #清空列表
print(s003)

del s003 #删除参数

#set关系
print(set('alex')==set('alexexex'))
print(set('alex')<set('alexwwww'))
print(set('alex') or set('alexwwww'))
print(set('alex') and set('alexwww'))
print(set('alexwww') in set('alex'))

