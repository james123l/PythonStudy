# list 栈内一个指向堆区列表的索引id 堆区列表内是指向堆区其他对象的id
# list 的两种创建方式
list01 = [1, 2, 3, 'hi']
list02 = list([1, 2, 3, 'hi'])

# 列表可以根据下标的方式寻找 左往右0开始 右往左-1
print(list01[0], list01[-4])

# 获取对象下标 返回从左往右第一个出现的下标
print(list01.index(1))
# print(list01.index('hi', 0, 3))  # 会报错 因为在[0，3）区间内查找 找不到hi

# list 切片操作 list[a:b:c] return 一个新的list
# 当步长为正数的时候 从[a,b)区间内进行筛选 默认步长是1 默认起始是0 默认终止是list的长度
# 当步长为负数的时候 起始默认为list最后一个元素 终止默认为第一个元素
list01 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(list01[0:7:2])        # [10, 30, 50, 70]
print(list01[0::-2])        # 默认终止是最后一个元素 [10]
print(list01[:2:-2])        # [90, 70, 50]

# list的 in 和 遍历
index = 0
if 50 in list01:
    for num in list01:
        if num == 50:
            print(index)
            break
        else:
            index += 1

# list增加
list01.append(100)  # 尾加 如果加入的是list 则会把这个list作为一个元素添加在list的末尾
list02.extend(list01)  # 在list02的末尾加入所有list01的元素
list01.insert(11, 110)  # 在11的位置加入元素 [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
list01[1:] = [11, 12]   # 把等号右值的list赋值给左值切片处 即下标为1的地方 并且去掉[1,end]的元素 [10, 11, 12]
print(list01)

# list 修改
list02[0] = 1       # 修改指定下标
list02[0:] = [10, 20, 30, 40, 50, 60, 70, 80, 90]  # 切片修改

# 列表生成
list02.clear()
list02 = [i for i in range(0, 100, 10)]  # i 是表达式 如果需要偶数 也可以写 2*i for i in range(0, 100)

# list 排序
list02.sort()   # 默认升序      list02.sort(reverse = True) 降序排序 false即为升序
newList = sorted(list02)       # sorted 内置方法进行升序排序       sorted(list02, reverse = True)  进行降序排序


# list 删除
list02.remove(90)   # 删除list02的第一个出现的50元素
list02.pop(7)       # 删除list中下标为8的元素 如果不写参数 则默认尾删
newList = list02[1:3]  # 切片删除法 只保留[1，3）的部分
list02[1:3] = []       # 切片法删除[1，3）的部分
list.clear()    # 清空列表
del list02      # 删除列表
