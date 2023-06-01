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