__all__ = ['add']       # all 列表决定了其他模块from MyAdd import * 时可以导入的东西有哪些
# 只有在all列表中的 才会被导入
# 导入包的方式1
# import ModuleDemo.MyAdd
# ModuleDemo.MyAdd.add()
# 导入包的方式2
# 在package的init.py种 需要添加all列表来控制包的导入行为,在这个package的init内会做实例
# from ModuleDemo import MyAdd


def add(a, b):
    return a + b

def test():
    print('not in all list')


if __name__ == '__main__':     # 如果程序以主程序运行才执行下列语句  # 每个模块都有一个变量__name__，如果模块不是被导入，会被解释器作为顶级模块执行 ，__name__ == '__main__'，即是main函数
    print(add(1, 2))           # 如果不以主程序运行 这个模块被导入后， 使用者控制台会输出 3
