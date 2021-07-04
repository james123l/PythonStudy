# 字符串有驻留机制
# 字符串常用操作
longStr = 'hello, world! hello!'
subStr = 'lo'
# 查找 find 和 index区别 find找不到返回-1 index 找不到抛出异常。 index找不到会抛出异常
longStr.index(subStr)       # 寻找第一次出现subStr的索引位置
longStr.find(subStr)        # 寻找第一次出现subStr的索引位置
longStr.rindex(subStr)      # 寻找第一次出现subStr的索引位置
longStr.rfind(subStr)       # 寻找第一次出现subStr的索引位置

# 大小写
str1 = longStr.upper()      # 全部转换大写 返回新的str
str1 = longStr.lower()       # 全部转换小写 返回新的str  str2 = longStr， =按值判断 返回true 。  str2 is longStr， is 按址判断 返回false 。
longStr.swapcase()          # 大写的转换为小写 小写的转换为大写
longStr.capitalize()        # 首字母大写 其他小写
longStr.title()             # 每个单词首字母大写 单词内其他字母小写

# 填充 不写填充符默认空格
str1 = 'hello'
str2 = str1.center(10, '*')        # 居中填充 **hello***
str2 = str1.ljust(10, '*')         # 左对齐填充 如果填充长度小于字符串长度则返回原串           hello*****
str2 = str1.rjust(10, '*')         # 右对齐填充 如果填充长度小于字符串长度则返回原串           *****hello
str2 = str1.zfill(10)              # 右对齐填充 如果填充长度小于字符串长度则返回原串 用0填充    00000hello  如果是对有符号的数字串添加 例如‘-890’.zfill(6) 则返回 ‘-00890’ 即包括符号一共6位切符号在前

# 分割字符串
str1 = 'hello world hello!'
strs = str1.split()             # 默认以空格作为分隔符 返回<class 'list'> ： ['hello', 'world', 'hello!']。
                                # strs = str1.split(sep='r')    设置r为分隔符
                                # strs = str1.split(sep='r',maxsplit = 1)    设置r为分隔符, 最多分割出一个字符串
                                # rsplit 可以从右分割 和split用法一致

# 判断字符串 返回布尔值
str1.isidentifier()     # 判断是不是合法标识符 字母数字下划线
str1.isspace()          # 判断是否是空格 回车 换行 tab等组成
str1.isalpha()          # 判断是否全部是字母组成
str1.isalnum()          # 判断是否全部由字母和数字组成
str1.isdecimal()        # 判断是否是十进制数字组成
str1.isnumeric()        # 判断是否是数组组成

# 替换与合并
str1 = 'hello,python,python,python'
str2 = str1.replace('python', 'java')       # 默认替换全部 ：hello,java,java,java
str2 = str1.replace('python', 'java', 2)    # 设置替换个数为2个：hello,java,java,python
list1 = ['hello', 'java', 'python']
str1 = ''.join(list1)                       # 合并函数 返回字符串 即用‘’ 链接元组或者list的内容 hellojavapython
str1 = '|'.join('python')                   # p|y|t|h|o|n

# 原始值和对应值
print(ord('a'))     # 找到a字符对应的编码值
print(chr(97))    # 找到67对应的字符值

# 字符串切片
str1 = 'hello world hello!'
print(str1[1:6:2])      # 切片,返回新的字符串 [1,6)区间内 步长为2 当步长为正数起始默认为0 终止默认end，负数则是起始默认end 步长默认1

# 字符串格式化
print('%d', 10)         # 占位符 和c语言printf一样
print('{0:10.3f}', format(3.141592653))     # {} 作为占位符 0代表索引 10代表宽度 .3代表三位小数 format规定数据

# 编码与解码
s = '天涯共此生'
byte = s.encode(encoding='UTF-8')       # 编码
s = byte.decode(encoding='UTF-8')       # 解码


