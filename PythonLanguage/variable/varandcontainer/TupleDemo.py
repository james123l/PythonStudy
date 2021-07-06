# 元组是不可变的（方便多任务时不需要锁） 存储的数据和list相似
# 元组的初始化方法
t = ('Python', 'JavaScript', 3306)      # 如果元组只含有一个元素 应该写为(10,) 需要括号和逗号 否则被认定为是int类型等原来的类型
t = 'Python', 'JavaScript', 3306        # 这样的写法括号可以省略
t = tuple(('Python', 'JavaScript', 3306))

# 元组的不可变性： 元组储存的是对象obj的地址 元组内的地址是不可变的 但是obj是可以改变的
t = (1, [2, 3], 4)      # 元组内index = 1 的元素是list
t[1].append(5)
print(t)
# 遍历
for item in t:
    print(item)