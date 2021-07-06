# 自定义异常类
class ShortInputException(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return f'your password length is{self.length}, but minimum length is {self.min_length}'

def main():
    try:
        con = input("input your password:")
        if(len(con)) < 3:
            raise ShortInputException(len(con), 3)      # raise方法抛出异常
    except Exception as result:           # 捕获try中的异常
        print(result)
    else:
        print('set password done')


main()
