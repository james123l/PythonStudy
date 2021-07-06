# 高阶函数demo 需求： 先按照指定方式运算数字，再返回两个数字的和
def addHigh(a, b, f):
    return f(a)+f(b)


print(addHigh(1, -1, abs))

# 内置高阶函数
# map 映射 把每个元素都进行计算 python3返回的是迭代器
def func(x):
    return x**2


list1 = [1, 2, 3, 4, 5]
result = map(func, list1)
print(result)       # <map object at 0x0000021BE86BFFA0> 迭代器地址
print(list(result))     # [1, 4, 9, 16, 25]

# reduce归约
import functools


def add(a, b):
    return a+b


result = functools.reduce(add,list1)
print(result)

# filter筛选 返回迭代器对象
def even(x):
    return x % 2 == 0


result = filter(even, list1)
print(result)       # <filter object at 0x00000170829BF940>
print(list(result))     # [2, 4]