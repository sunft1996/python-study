# Demo1: 继承父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# 继承
class Student(Person):
    def __init__(self, name, age, student_id):
        # 调用父类的__init__方法
        super().__init__(name, age)
        self.student_id = student_id

    # def say_hello(self):
    #     super().say_hello()
    #     print(f"My student ID is {self.student_id}.")


person1 = Person("Alice", 25)
# 不需要传递self
person1.say_hello()

student1 = Student("Bob", 20, "1234567")
student1.say_hello()


# Demo2: 抽象基类
# 概念：抽象基类是不可实例化的类，其主要的作用是为继承它的子类提供一些规范、属性或方法等。
# 通常用抽象基类作为接口
# 任何继承该抽象基类的子类，都需要实现其中定义的抽象方法，以接口满足的要求
from abc import ABC, abstractmethod
class AnimalInterface(ABC):
    # 该装饰器用来定义抽象方法，子类必须实现抽象方法
    @abstractmethod
    def run():
        pass

class Dog(AnimalInterface):
    def __init__(self):
        self.name = 'XiaoHei'
    # 不设置会报错 
    def run():
        print('XiaoHei is running...')

dog1 = Dog()


# Demo3: 静态属性和静态方法
# 都可以直接被 类 和 实例对象 调用
# 静态属性 被修改后，会影响到所有实例对象
# 静态方法 不能访问self指针
class ClassStaticDemo(ABC):
    class_var = 0
    # 定义静态方法 
    @staticmethod
    def static_method(x, y):
        return x + y

print(ClassStaticDemo.class_var)
print(ClassStaticDemo.static_method(1,2))

# Demo4: 枚举类
import enum
class Operation(enum.IntEnum):
    # 默认情况下，第一个枚举成员的值为 0，后续枚举成员的值依次递增
    HANDSHAKE = 0
    HANDSHAKE_REPLY = 1
    HEARTBEAT = 2
    HEARTBEAT_REPLY = 3
    SEND_MSG = 4
    ERROR = -1

# 与字典对比
dict1 = {"name": "Tom", "age": 18, "gender": "male"}

# 报错，字段无法使用key来访问
# print(dict1.name) 
print(dict1['name'])
print(Operation.HANDSHAKE)