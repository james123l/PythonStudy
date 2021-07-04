# python 是按址传递
# 当传递的是可变的对象 函数内的更改可以对调用者的参数进行更改
# 当传入的是不可变对象 例如输入的是字符串s = ’hi‘ ,在函数中s即便是赋值了其他字符串 也不会对调用者的变量进行更改

def judgeoddeven(a=1, b=2, c=3, d=4):      # a=1是默认参数，调用的时候就可以无参，一/二/三/四个参数 可以只写def func(a, b, c, d) 这样就没有默认值 。
    list1 = [a, b, c, d]
    odd = []
    even = []
    i = 0
    while i < 4:
        if list1[i] % 2:
            even.append(list1[i])
        else:
            odd.append(list1[i])
        i += 1
    return odd, even         # return语句 如果没有返回值可以不写 可以返回一个值 如果返回多个值则返回的是一个元组


def printertuple(*args):       # 个数可变的位置形参 传入的args 默认为元组 可变参数前可以加固定参数，可变参数只能是一个
    print(args, type(args))


def printerdict(**kwargs):       # 个数可变的关键字形参 传入的args默认为字典
    print(kwargs, type(kwargs))


def printerboth(*args, **kwargs):   # 两个都有的时候 先写位置形参 再写关键字形参
    print(args, type(args))
    print(kwargs, type(kwargs))


# 测试
res = judgeoddeven(b=15)            # 此处规定了b的值 即judgeoddeven(a=1, b=15, c=3, d=4) 除了b 其他都是默认值
print(res, type(res))
printertuple(1, 2, 3)
printerdict(a=1, b=2, c=3)
printerboth(1, 2, 3, a=1, b=2, c=3)
