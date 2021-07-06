# os操作系统模块
import os
os.system('notepad.exe')            # 通过命令行打开记事本
os.getcwd()                         # 获取当前工作目录
os.listdir('../moduleDemo')         # 返回指定路径下的文件和目录信息
os.mkdir('newDir')                  # 创建目录 如果已经存在则无法创建
os.makedirs('newDir/A/B')           # 创建多级目录
os.rmdir('newDir/A/B')              # 删除目录
os.removedirs('newDir/A')         # 删除多级目录
os.chdir("F:\\python\PythonLanguage\\objectoriented\\moduleDemo\\ModuleDemo.py")   # 将path设置为当前工作目录