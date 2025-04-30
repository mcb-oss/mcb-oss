#变量

#全局变量
param = 1

def method():
    #局部变量
    param = 2
    print("内部：",param)

#在方法内修改全局变量！！
def change():
    #声明param为全局变量
    global param
    param = 3
    print("内部：",param)

method()
change()
print("外部：",param)



#在方法内声明全局变量！！
def method2():
    #声明count为全局变量
    global count
    count = 2

#调用过后，方法中声明的全局变量开始生效，外部任意地方可以访问到
method2()
print("count=",count)



print("---------nolocal---------")
def out():
    a = 1
    def inner():
        #nonlocal关键字内部函数修改外部函数局部变量值
        nonlocal a
        a = 2
        print(a)
    inner()
    print(a)

out()