# 列表生成式

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
m_list = [x * x for x in range(1, 11)]
print(m_list)

# [4, 16, 36, 64, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])


"""
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
if条件放在for循环前面表示表达式，即每个循环元素经过表示式，表达式必须有个返回结果
"""
print([x if x % 2 == 0 else -x for x in range(1, 11)])

# [2, 4, 6, 8, 10],if条件放在for循环后面表示筛选条件，不能加else
print([x for x in range(1, 11) if x % 2 == 0])


# 小测试
L1 = ["Hello", "World", 18, "Apple", None]
# [表达式 数据源 过滤条件]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ["hello", "world", "apple"]:
    print("测试通过!")
else:
    print("测试失败!")
