# 导入模块的方式
import time

import MyAdd              # 导入整个模块
from MyAdd import add     # 导入add方法 from后面也可以是变量，包，函数等
# import moduleDemo.MyAdd  # 导入 模块名.包名
# 在终端输入 pip install schedule # 安装schedule模块
import schedule

print(add(10, 20))      # 如果模块里不以主程序运行 这里会打印导入模块内的语句 多输出一个 3


def send():
    print('sending message')


# 第三方包使用
schedule.every(3).seconds.do(send)
while True:
    schedule.run_pending()
    time.sleep(1)

