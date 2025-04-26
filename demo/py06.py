#类型转换

print(int(1.23))

print(int(True))
print(int(False))

print(float(3))
print(float("1.45"))

print(str(3.14))

#任意非0都为true
print(bool(0))

#计算表达式，一个有效的python表达式
x = 1
y = 2
print(eval('x + y'))


print(list("test"))
print(tuple("test"))
print(dict(name="bingbing",b=2,c=3))
#根据list生成字典，元组、set同理
dict_list = [   
    ('name','bingbing'),
    ('age',18),
    ('gender','male')
]
print(dict(dict_list))
print(set("test"))