# 切片

l = ["Michael", "Sarah", "Tracy"]

print(l[-1:])

# 从索引0开始取，直到索引3为止，但不包括索引3,如果第一个是0可以省略
print(l[:3])
# Sarah ,从索引1开始取，直到索引2为止，但不包括索引2
print(l[1:2])

""" 
["Michael" -3, "Sarah" -2, "Tracy" -1]
输出："Michael", "Sarah"
从索引-3开始取，直到索引-1为止，但不包括索引-1
"""
print(l[-3:-1])

tList = list(range(101))
# 前十个数
print(tList[:10])
# 后十个数
print(tList[-10:])

# 前十个，每两个拿一个数
ll = tList[:10:2]
print(ll)

tList.append(101111)
# 复制一份list地址，会随着原list改变
copyList = tList[:]
print("copyList:", copyList)

# 字符串也可以看成一个列表
str = "ABCDEFG"[:3]
print(str, list(range(len(str))))


# 去除首位空格,不可用strip()
def trim(s):
    pre = 0
    end = 0
    for p in range(len(s)):
        if s[p] != " ":
            pre = p
            break
    # 当step是-1的时候，range会递减，直到当前值小于等于stop。所以当start是4，stop是-1，step是-1时，序列会是4,3,2,1,0，然后停止，因为下一个是-1
    for e in range(len(s) - 1, -1, -1):
        if s[e] != " ":
            end = e + 1
            break
    return s[pre:end]


# 测试:
if trim("hello  ") != "hello":
    print("测试失败!")
elif trim("  hello") != "hello":
    print("测试失败!")
elif trim("  hello  ") != "hello":
    print("测试失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败!")
elif trim("") != "":
    print("测试失败!")
elif trim("    ") != "":
    print("测试失败!")
else:
    print("测试成功!")
