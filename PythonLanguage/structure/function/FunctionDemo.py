# python 是按址传递
# 当传递的是可变的对象 函数内的更改可以对调用者的参数进行更改
# 当传入的是不可变对象 例如输入的是字符串s = ’hi‘ ,在函数中s即便是赋值了其他字符串 也不会对调用者的变量进行更改

def judgeoddeven(a=1, b=2, c=3, d=4):      # a=1是默认参数，调用的时候就可以无参，一/二/三/四个参数 可以只写def func(a, b, c, d) 这样就没有默认值 。
    # 如果有个全局变量a=1在函数外 函数内声明a = 20，此时函数内的a依然是局部的 调用后不会改变全局变量的值。
    global var
    var = 'global var'   # 函数内声明全局变量需要分开声明和赋值 函数外的都是全局变量
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


def printerdict(**kwargs):       # 个数可变的关键字形参(键值对) 传入的args默认为字典
    print(kwargs, type(kwargs))


def printerboth(*args, **kwargs):   # 两个都有的时候 先写位置形参 再写关键字形参
    print(args, type(args))
    print(kwargs, type(kwargs))


def printer(a, b, *, c, d):     # *之后的参数必须使用关键字传参
    print(a, b, c, d)


def printermore(a, b, *, c, d, **args):   # *之后不能用*args 有歧义。 可以使用**args
    print(a, b, c, d)
    print(args, type(args))


# 测试
res = judgeoddeven(b=15)            # 此处规定了b的值 即judgeoddeven(a=1, b=15, c=3, d=4) 除了b 其他都是默认值
res = judgeoddeven(*[1, 2, 3, 4])    # 把列表的元素作为参数传递进入函数，需要加* ，否则列表被当作一个参数
argdict = {'a': 10, 'b': 2, 'c': 30, 'd': 4}  # 传入字典 需要** key是参数名 value是形参对应的值 10 2 30 4是函数内abcd对应的值
res = judgeoddeven(**argdict)
print(res, type(res))
# 元组 字典拆包
odd, even = judgeoddeven(*[1, 2, 3, 4])     # 元组拆包 直接用同等数量变量接受  字典拆包拿到的是key
print(odd)
print(even)

printertuple(1, 2, 3)
printerdict(a=1, b=2, c=3)
printerboth(1, 2, 3, a=1, b=2, c=3)
printer(1, 2, c=3, d=4)
printermore(1, 2, c=3, d=4, g=7, f=9)
