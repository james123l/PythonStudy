# coding:utf-8
# 写在文件头的文件编码注释

# python 字符串可以单引 双引
# print 输出并换行
print('hello,world')
print("hello,world")

# 输出多个字符串在一行
print('hello ', 'world')

# 把数据写入文件 参数是 路径，模式
# a+ ： 不存在则创建 存在则在文件末尾追加
# fp = open('D:/test.txt', 'a+')
# print('hello,world', file=fp)
# fp.close()

# 转义字符
print('hello\tworld')   # tab
print('hello\nworld')   # 换行
print('hello\rworld')   # 会输出world 因为\r代表擦除前面的字符
print('helloo\bworld')   # \b 代表抹除前一个字符 所以会输出 helloworld
print('he said:\"you can go to http:\\\\www.google.com\".')  # he said:"you can go to http:\\www.google.com".
# 原字符
# 在前面写上r 或者R 就可以让转义字符失效
print(r'hello,\t world!')  # hello,\t world!
# 注意：原字符结尾不能是单个的\ 但是可以是\\。  例如： print(r'hello,\t world!\') 是错误的
print(r'hello,\t world!\\')   # hello,\t world!\\

# input函数 默认获取的是字符串，即下面a b 都默认是字符串
a = input("input a number")
b = input('input another number')
print(int(a)*int(b))


