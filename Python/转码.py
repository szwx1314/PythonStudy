# Author:YSY

'''
str = "杨士永"

def test(x):
    x+=1
    return x

print(test(2))

print("这个程序是 %s %s" %(str,str))


def test2():
    return 1,'ysy',['ysy','dyy']

print(test2())

def test3():
    return test2()

print(test3())
'''
'''
def test222(x,y=2,z=3):
    print(x)
    print(y)
    print(z)

test222(1)


def test333(*args):
    print(args)

test333(1,2,3,4,5,6,7,8,9,0)
'''


def test1():
    print(logger())
    print('test1',1111)



def logger():
    print('test2',22222)


test1()




