# 创建字典的方式
# 字典的key必须是不可变序列 例如字符串 元组
kvs = {'a': 1, 2: 'b', 3: 'c'}
kvs = dict(a='a', b='b', c='c', d='d')
# 映射方式
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
# 映射方式一
ab = zip(a, b)      # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
kvs = dict(ab)      # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# 映射方式二 : 字典生成式
dictAB = {aitem:bitem for aitem, bitem in a, b}
# 可迭代对象
kvs = dict([('one', 1), ('two', 2), ('three', 3)])   # {'three': 3, 'two': 2, 'one': 1}

# 获取元素dict[key]  区别： 如果key不存在 get返回none []则会报错
print(kvs['one'])
print(kvs.get('one'))       # print(kvs.get('one'), 15) 如果不存在 默认返回15

# 遍历
for item in kvs:
    print(item)                 # 输出key
    print(kvs.get(item))        # 输出value

# 判断 删除 修改 新增
print('five' in kvs)
print('five' not in kvs)
kvs['five'] = 6   # 增加
kvs['five'] = 5   # 修改
del kvs['five']   # 删除
kvs.clear()       # 清空

# 字典视图
keys = list(kvs.keys())         # type(kvs.keys()) 是dict_keys 类型 可以转换为list
values = list(kvs.values())     # type(kvs.values()) 是dict_values类型 可以转换为list
items = list(kvs.items())       # type(kvs.items()) 是dict_items 类型 ,实际上是元组 可以转换为list 输出形式是[('abc',123)...]


