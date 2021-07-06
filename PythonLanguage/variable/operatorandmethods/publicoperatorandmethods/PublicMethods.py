# 对于容器和字符串
# len方法 对于list set dict str tuple 可以统计长度
# 容器类型之间可以通过set() list() tuple() 相互转换
str1 = 'hello,world'
print(len(str1))
print(min(str1))    # 求最小值 也有max函数
for i in enumerate(str1):       # (0, 'h') 打印下标+数据组成的元组
    print(i)
del str1        # 删除str1对象 也可以写括号 对于dict 也可以删除 del dict[key] 这样只删除这个键值对

# 列表推导式
list1 = [i for i in range(1, 10, 1)]
list1 = [i for i in range(1, 10, 1) if i % 2 == 0]        # 带if的
list1 = [(i, j) for i in range(1, 3) for j in range(3)]   # 多重循环[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 字典的映射方式推到
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
# 映射方式一
ab = zip(a, b)      # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
dict1 = dict(ab)      # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
# 映射方式二 : 字典生成式
dict1 = {a[i]: b[i] for i in range(len(a))}

# 字典的目标数据提取
collectmorethanb = {key: value for key, value in dict1.items() if value > 'b'}
print(collectmorethanb)

