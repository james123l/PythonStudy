# python的异常处理
import traceback  # 导入traceback模块
try:        # try 可以配合 except 和finally
    a = int(input("input numerator"))
    b = int(input("input denominator"))
    res = a / b
except BaseException as e:  # as 起别名 except语句处理异常，可以多重except语句，从小到大捕获（例如 zerodivision <valueerror< baseexception）
    print("error! information", e)      # 1打印错误信息
    traceback.print_exc()               # 2打印错误信息
else:       # 如果没有出现异常 会执行到这一步。如果出现异常则不执行。  else语句可以省略
    print(res)
finally:
    print("function closed!")