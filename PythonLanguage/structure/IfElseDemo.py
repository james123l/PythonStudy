a = int(input("input a number(0-100):  "))
if a >= 0 and a <= 100:
    if a % 2 == 0:
        print(str(a) + "  is even number")
    elif a % 2 == 1:
        print(str(a) + "  is odd number")
    else:
        pass    # pass语句是占位符 使得程序不报错
else:
    print("wrong number")
#  if else 的简略表达式
print(str(a)+'> 50' if a > 50 else str(a)+'<=50')
