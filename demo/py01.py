print("Hello World")
print("Hello World")

# r'' 内部代码不编译
print("y5s" r"/n")

flag = True
print(flag)

x = 20
x += 1
print(x)


a = "ABC"
b = a
a = "XYZ"
print(b)
# 商为浮点
print(10 / 3)
# 商向下取整
print(10 // 3)

# 常量
PI = 3.14159265359
print(PI)

# ----------- List
team = ["a", "b", "c"]
# 是list类型！！
print(type(team))
# 获得末尾
print(team[-1])
team.append("d")
print(team)
team.insert(1, "a1")
print(team)
# 移除末尾
team.pop()
# 移除指定位置
team.pop(1)
print(team)


print("----List集合-----")
# list里面的元素的数据类型也可以不同
L = ["Apple", 123, True]
# list里面的元素的数据类型也可以不同
s = ["python", "java", ["asp", "php"], "scheme"]

# 循环list
for l in L:
    print("list参数", l)

# 循环list,既要下标 又要数值
for index, value in enumerate(L):
    print(index, ":", value)

print("----tuple不变集合-----")
# tuple 不可变数组
classmates = ("Michael", "Bob", "Tracy")
# 只有1个元素的tuple定义时必须加一个逗号,避免以为是1
t = (1,)


# ------判断--------
# 只要t是非零数值、非空字符串、非空list等，就判断为True，否则为False
if t:
    print("True")


age = 15

match age:
    case x if x < 10:
        print(f"< 10 years old: {x}")
    case 10:
        print("10 years old.")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print("11~18 years old.")
    case 19:
        print("19 years old.")
    case _:
        print("not sure.")


print("----循环-----")
# 循环
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# ---disc（map）---
d = {"Michael": 95, "Bob": 75, "Tracy": 85}
print(d["Michael"])
# 可以放!不同类型
d[1] = 100
print("disc（map）", d)
# getordefault()
print(d.get("mcb", 10000))


# --------- set集合
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(s))


# 支持将list作为入参
forList = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(forList), forList)


s1 = {1, 1, 2, 2, 3, 3}
print(s1)

# 字节!串（bytes） 表示不可变的字节序列，通常用于处理二进制数据。
data = b"hello"
raw_data = bytes([65, 66, 67])  # b'ABC'
print(type(data), data)
print(type(raw_data), raw_data)

# 字节!数组（bytearray) 类似于 bytes，但它是可变的
mutable_data = bytearray(b"hello")
print(mutable_data)
mutable_data[0] = 72  # 修改第一个字节为 'H'
print(mutable_data)

# 三目表达式  value_if_true if condition else value_if_false
print("是的" if True else "不是")
