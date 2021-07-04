from decimal import Decimal

# 数据类型的信息显示方法
name = 'Maria'
print('var\t value  =\t', name)
print('var\t bool   =\t', bool(name))   # null none 0 false的布尔值都是false python一切皆对象 每个对象都有一个布尔值
print('memory addr =\t', id(name))
print('class  type =\t', type(name))


# int,float,bool类型
a = 10
b = 1.1
c = 2.2
print(b+c)   # 会出现 计算不精确的现象 可以使用导入Decimal模块解决
flagTrue = True     # 1
flagFalse = False   # 0
print(True+False+1)  # python 的布尔类型可以转换为int类型参与运算

# 导入decimal模块
# from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 字符串 可以使用单引号 双引号 三引号
# 字符串索引 从左到右是从0 开始 从右往左是从-1开始递减
strPy = '人生苦短，我用python'
strCut = strPy[0:4]  # 截取[0，4）子串 也可以用负号写
print(strCut)
strPy = "人生苦短，我用python"
# 三引号 可以让字符串分多行
strPy = """人生苦短，
我用python"""
strPy = '''人生苦短，
我用python'''

# 类型转换
# str() 参数可以是任何类型的数据
# int() 参数可以是float 或者是整数字符串（不能有小数）
# float() 参数可以是int 或者数值型str
floatStr = 123.2
print(str(floatStr))