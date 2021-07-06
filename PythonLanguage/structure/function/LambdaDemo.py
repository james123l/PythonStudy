# lambda匿名函数 一般来说lambda体内只可以有一行代码 但是可以用元组和列表使其成为多行函数
# 无参
func = lambda: 100     # return 可以省略
# 带参 可以设置默认值
func = lambda a, b, c = 10: a+b+c
# 可变长参数 arg返回元组 kwarg返回字典
func= lambda *args: args
func= lambda **kwargs: kwargs
# 带判断的lambda
func = lambda a, b : a if a>b else b

students = [
    {'name': 'James', 'age': 20},
    {'name': 'Tom', 'age': 21},
    {'name': 'Kate', 'age': 22}
]
# lambda为list排序
# 升序
students.sort(key=lambda x: x['age'])
# 降序
students.sort(key=lambda x: x['age'], reverse=True)
