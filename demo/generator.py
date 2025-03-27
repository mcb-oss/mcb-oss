# 生成器

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
"""
L = [x * x for x in range(10)]
# 列表生成式，结果为列表类型
print(type(L))

g = (x * x for x in range(10) if x > 5)
# 生成器类型
print(g)

# 根据next方式获取下一个元素时，如果没有更多元素，抛出StopIteration
# 36
print(next(g))
# 49
print(next(g))

for n in g:
    print(n)


"""

著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

a, b = b, a + b 等同于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
"""


# 普通方法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return "done"


fib(6)


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 生成器函数要使用yield关键字，yield关键字表示生成器函数
        yield ("fib_generator", b)
        a, b = b, a + b
        n = n + 1
    return "done"


# 注意输出值式yield的返回值，而不是return！！！
for i in fib_generator(6):
    print(i)
