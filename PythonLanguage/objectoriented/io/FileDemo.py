# 文件
file = open('a.txt', 'w')
print(file.write('hello,world!'))
file.close()

src_file = open('src_img.png', 'rb')
target_file = open('copy.png', 'wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

# open 函数的5种参数
# r 只读模式 文件指针在文件头
# w 只写模式 文件指针在文件头 无则创建 有就会覆盖
# a 只写模式 文件指针在文件头 无则创建 有就会尾加
# b 二进制形式 不能单独使用 需要和别的一起 例如 rb rw
# + 以读写的方式打开 不能单独使用 需要其他的模式一起 例如 a+

file = open('a.txt', 'r')
print(file.read(2))          # 读取2个字符
file.seek(0)                # 重置文件指针 按照字节 如果储存的是中文一个字2个字节 seek(1)会出现错误 因为把第一个汉字的2个字节分成两半
file.tell()                 # 返回文件指针现在的位置
file.flush()                # 把缓冲区的信息写入文件
print(file.readline())      # 读取一行文件内容
print(file.readlines())     # 读取所有行 并且作为列表返回值
file.close()
file = open('a.txt', 'a')
file.write('hello,world!')  # 写入一行
file.writelines(['hi\n', 'I\'m James', 'How are you?'])  # 不添加换行符不会自动换行
