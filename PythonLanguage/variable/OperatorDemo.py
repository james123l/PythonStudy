# python有加减乘除取模运算符
# 其中/可以获取小数， //是整除运算(同为正数9//4 向下取整=2， 一正一负 -9//4 向下取整 -3)
# ** 代表次幂
print(11/2)     # 5.5
print(11//2)    # 5
print(2**2)     # 2^2

# python 赋值运算 也有 //=， /=等等
a = b = c = 20
a, b = 10, 20
a, b = b, a

# 比较运算符 ！= ，== ,> < 。 python有个特殊的运算符 is/is not 判断id是否相等（python是oop 所以栈内是指向堆区的指针，堆区模型是 有数据 类型 id组成）
a = 10
b = 10
print(a is b)   # Ture（id标识相等） ,因为解释器发现堆区已经有了value=10 的对象 就不会创建新的 而是把 a指向的空间赋值给b
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(a is not b)      # 因为a b 的id不相等

# 布尔运算符
a = 10
b = 10
s = 'hello,world!'
print(a == 1 and b == 2)    # 与
print(a == 1 or b == 2)     # 或
print(not a == 1)           # 非
print('5'  in s)            # s包含‘5’
print('5' not in s)         # s不包含‘5’

