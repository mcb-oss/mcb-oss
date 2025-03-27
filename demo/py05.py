from collections.abc import Iterable

# collections.abc模块的Iterable类型，判断一个对象是否是可迭代对象

# 迭代

d = {"a": 1, "b": 2, "c": 3}

# 迭代字典的key
for index in d:
    print(index, ":", d[index])


# 迭代字典的values
for value in d.values():
    print(value)

# 迭代字典的键值对
for k, v in d.items():
    print(k, v)

# 迭代字符串
for ch in "ABC":
    print(type(ch), ch)

print(isinstance(12313, Iterable))

# 单列集合循环
for i, value in enumerate(["A", "B", "C"]):
    print(i, value)


def findMinAndMax(L):
    if L == []:
        return (None, None)
    min, max = L[0], L[0]
    for i in L:
        if i > max:
            max = i
        elif i < min:
            min = i
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
