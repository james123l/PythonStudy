# python循环也可以使用 break continue语句 和java一样 作用域仅仅是本层循环

# while 循环
a = 0
while a < 10:
    a += 1
print("while loop finish")

# forin 循环 需要in后面是可迭代对象 例如字符串 range
for ch in "hello,world":
    print(ch)
for _ in range(10):   # 在不需要循环变量的时候可以使用_ 代替变量
    print("life is short, I use Python")


# 循环与else搭配
# 当循环正常结束的时候 执行else
# 循环被break的时候不执行else
for _ in range(3):
    if 3 > 4:
        break
else:
    print("loop not break")
