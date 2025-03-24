import math
# 定义函数

def test(x):
    print('test函数答应：',x)


print('函数执行返回值：',test(100))

# 空函数 占位
def my_pass(args):
 pass

def my_abs(x):
   if not isinstance(x,dict):
      raise TypeError('bad operand type')
   print("校验通过，参数：",x)

my_abs({1:1,2:2})

# 可返回多个值,  angle 默认参数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print('move',move(1,100,3))

# 默认参数必须指向不变对象！！
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())


print('-------可变参数 --------')
# 这种情况numbers随着传入参数类型随之而变
def calc(numbers):
   print(type(numbers))

calc(1)

# *args 用于接收任意数量的位置参数，参数会被打包成一个元组
# **kwargs：用于接收任意数量的关键字参数，参数会被打包成一个字典
def example(arg1, *args, **kwargs):
    print("First argument:", arg1,',type:',type(arg1))
    print("Additional positional arguments:", args, ',type:',type(args))
    print("Additional keyword arguments:", kwargs, ',type:',type(kwargs))
    kwargs['test']='test1'
    print(kwargs)

example(1, 2, 3, a=1, key2="value2")


