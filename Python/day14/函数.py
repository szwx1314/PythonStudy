#http://www.cnblogs.com/yuanchenqi/articles/5828233.html

#函数
def f():
    print('OK')
f()

#高阶函数
#1-------------
def foo3():
    def inner():
        return 8
    return inner
ret = foo3()
print(ret())

#2--------------
def f1(n):
    return n*n

def f2(n):
    return n+n

def f0(a,b,funt):
    return funt(a)+funt(b)

print(f0(2,3,f1))
print(f0(2,3,f2))