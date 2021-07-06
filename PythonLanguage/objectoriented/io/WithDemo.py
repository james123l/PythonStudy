# with 和上下文管理器
'''
ContentManager 实现了特殊方法 __enter__() __exit__() 称为该类的对象遵守了上下文管理器协议
该类的对象被称为上下文管理器
'''


class ContentManager(object):
    def __enter__(self):
        print('enter function')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit function')

    def show(self):
        print('show function')


with ContentManager() as file:
    file.show()     # 进入语句前 解释器会先执行enter函数 然后执行语句后会执行exit函数。 enter和exit不论是否异常都会执行

# 上下文管理器实现文件拷贝
with open('src_img.png','rb') as srcFile:
    with open('copy.png','wb') as targetFile:
        targetFile.write(srcFile.read())