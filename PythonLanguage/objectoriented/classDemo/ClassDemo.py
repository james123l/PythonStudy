# python的类也是一个对象， 类的实例是一个以类对象为模板建造的对象，有自己的变量，并且有一个指针指向类对象
# 创建类
class Person:       # 默认继承object
    pass    # 最简单的Person基类


class BYUStudent(Person):       # 继承Person
    state = 'Idaho'     # 类属性 是类对象的成员 所有类实例都共享

    def __str__(self):
        return 'name:{0},age:{1}'.format(self.name, self._BYUStudent__age)

    def __init__(self, name, age):
        self.name = name       # 实例属性 不属于类对象 属于实例
        self.__age = age       # __表示不希望类的外部访问 相似于私有 但是外部可以通过_BYUStudent__age访问

    # 实例方法 需要有实例才能使用
    def info(self):
        print('Student:', self.name, ":", self._BYUStudent__age)

    # 类方法
    @classmethod
    def classfunc(cls):
        print("class method")

    @staticmethod
    def staticfunc():
        print("static method")


class Worker(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)     # 调用父类方法
        self.job = job
    pass


class PartTimeStudent(Worker, BYUStudent):  # 多继承
    def info(self):         # 方法重写
        print('PT Student:', self.name, ":", self._BYUStudent__age)
    pass


def eat():
    print('eat function')


# james = BYUStudent()    # 无实例属性 仅当__init__函数没有在类中声明时可以使用
# print(james)    # <__main__.BYUStudent object at 0x000001CD896EAD30>
james = PartTimeStudent("james", 25, "chef")
print(james)                # 默认调用__str__方法
print(dir(james))           # 查看james的所有成员属性和方法
james.gender = 'male'       # 动态绑定属性
james.eat = eat             # 动态绑定方法
james.eat()


james.info()
BYUStudent.info(james)
BYUStudent.staticfunc()     # 类名.方法 可以直接访问静态和类方法
BYUStudent.classfunc()

