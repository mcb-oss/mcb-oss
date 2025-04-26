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

print("count",t.count(1))
print("len",len(t))


# ------判断--------
# 只要t是非零数值、非空字符串、非空list等，就判断为True，否则为False
if t:
    print("True")




print("---- match -----")

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
print("-----disc（map）---")
d = {"Michael": 95, "Bob": 75, "Tracy": 85}

# put：
# 可以放!不同类型
d[1] = 100
# 如果键存在，返回其值，如果键不存在，插入键并设置默认值，然后返回默认值
d.setdefault("Bob", "bingbing") 

print("disc（map）", d)

# get：
print(d.get("mcb", 10000))
print(d["Michael"])

#del:
#删除的key必须是包含的，不然会抛出keyerror
del d["Tracy"]
print("after del",d)

#pop:
#移除并返回移除的值，如果键不存在字典中则返回默认值，没有提供默认值则会抛出keyerror
d["test"] = 100
a = d.pop("test")
print("pop value",a)
#提供默认值
result = d.pop("aaaaa","not found")
print("pop has default:",result)

#clear:
d.clear()
print("after  clear",d)


# 常规使用
info = {"name":"bingbing","age":18}
print("name" in info) #字典中是否包含对应key，containKey同理
print("name" not in info)

print(len(info)) #键值对个数

# 键值对遍历
for key, value in info.items():
    print(key, value)   

# --------- set集合
print("-----set---")
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(s))

#add;
s.update({11,12,13})
print("after update",s)

#remove: 有则删除，不存在则报错
a = s.remove(1)
print("remove",a)

#discard: 有则删除，不存在则不报错
a = s.discard(15)
print("discard",a)

#交集
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {6, 7, 8, 9, 10}
print("交集",s1 & s2)
print("交集",s1.intersection(s2))

#并集
s3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s4 = {6, 7, 8, 9, 10}
print("并集",s3 | s4)
print("并集",s3.union(s4))

# 支持将list作为入参
forList = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("forList",forList)


print("-------bytes和bytearray---------")

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

print("y" if True else "n")
