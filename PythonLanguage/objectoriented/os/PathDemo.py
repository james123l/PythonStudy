# os的path模块
import os.path as opth
strPath = opth.abspath('PathDemo.py')      # 获取绝对路径
opth.exists(strPath)                       # 判断是否存在这个文件或者文件夹
opth.join('a.txt', 'b.txt')                # 拼接两个文件或者文件夹的目录
opth.split('a.txt')                        # 拆分目录和文件名
opth.splitext('a.txt')                     # 拆分文件名和拓展名
opth.basename(strPath)                     # 提取文件名
opth.dirname(strPath)                      # 提取路径且不包含文件名
opth.isdir(strPath)                        # 判断是不是路径

# 迭代器遍历文件
import os
path = os.getcwd()
first_files = os.walk(path)     # 获取迭代器对象 返回值是元组
for dirpath,dirname,filename in first_files:
    for dir in dirname:
        print(opth.join(dirpath, dir))
    print('---------------------------')
    for file in filename:
        print(opth.join(dirpath, file))

# 打包 需要第三方包
# pip install PyInstaller
# 打包命令： pyinstaller -F 工程路径
