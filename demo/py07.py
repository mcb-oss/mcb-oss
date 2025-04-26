import copy

#深拷贝 浅拷贝
list = [1,2,[3,4]]
# copy.copy() 浅拷贝,基础数据类型拷贝，引用数据类型还指向原始地址
copy_list = copy.copy(list)

#深拷贝，全部数据完全独立（无论基础数据类型还是引用数据类型）
deep_copy_list = copy.deepcopy(list)