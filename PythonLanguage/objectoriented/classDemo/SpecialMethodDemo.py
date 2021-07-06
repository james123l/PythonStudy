class A:
    pass


class B:
    pass


# new和init方法：调用C()初始化的时候， 先把C的class即cls参数传递给new方法 返回一个Obj之后把这个obj作为self传入init方法 进行实例属性赋值
class C(A, B):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):   # 实现对象相加
        return self.age + other.age

    def __len__(self):          # 使对象可以打印长度
        return len(self.name)


c1 = C("jack", 20)
c2 = C("jim", 21)
# 特殊属性
print(c1.__dict__)    # 实例对象的属性字典
print(C.__dict__)
print(c1.__class__)   # 打印所属类
print(C.__bases__)      # 显示父类元组
print(C.__mro__)        # C的层次结构
print(A.__subclasses__())   # A当前子类
# 特殊方法
print(c1 + c2)          # 也可以 c1.__add__(c2)
print(c1.__len__())     # 计算长度

c1.a = A()  # 添加引用类型
import copy
# 潜拷贝
temp = copy.copy(c1)
print(id(c1.a))
print(id(temp.a))
# 深拷贝
temp = copy.deepcopy(c1)
print(id(c1.a))
print(id(temp.a))
