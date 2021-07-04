# set 哈希表 储存不重复无序元素
# 创建方法
set1 = {1, 2, 3, 4, 4, 5}       # {1, 2, 3, 4, 5} 自动去重
set1 = set()                    # 定义空集合的唯一方法
set1 = set('python')            # {'p', 'y', 't', 'h', 'o', 'n'} 无序
set1 = set(range(6))            # {0, 1, 2, 3, 4, 5}
set1 = set([1, 2, 3, 4, 4, 5])  # set函数可以把list/tuple 转化为set  set((1, 2, 3, 4, 4, 5))

# set常用方法
print(1 in set1)        # print(1 not in set1)
set1.add(0)             # add one item
set1.update([6, 7])     # add at least one item 要求参数是可迭代 iterable 元组 列表 set 都可以
set1.remove(7)          # 删除一个元素 如果元素不存在 抛出异常
set1.discard(7)         # 删除一个元素 如果元素不存在 不会抛出异常
set1.pop()              # 删除任意元素
set1.clear()            # 清空

# set的关系判断
set1 = {1, 2, 3, 0}
set2 = {1, 2, 3, 5}
print(set2 == set1)             # True  print(id(set1), id(set2))不相等 按值比较
print(set1.issubset(set2))      # 判断是否为子集   True （相等也算）
print(set1.issuperset(set2))    # 判断是否为超集   True （相等也算）
print(set1.isdisjoint(set2))    # 判断是否没有交集 False

# set数据操作 求交集 并集 差集
# 求交集
print(set1.intersection(set2))
print(set1 & set2)
# 求并集
print(set1.union(set2))
print(set1 | set2)
# 求差集
print(set1.difference(set2))
print(set1 - set2)
# 求对称差集
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

# set 生成式
set1 = {i for i in range(0, 100, 2)}

