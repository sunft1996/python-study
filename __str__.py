# __str__ 是一个特殊方法（也称为魔术方法或魔法方法），用于定义对象的字符串表示形式。
# 这个方法在 Python 中是预定义的，可以被用户自定义类所重写。
# 当我们调用内置的 str() 函数或使用 print() 函数打印一个对象时，Python 会自动调用该对象的 __str__ 方法来获取其字符串表示形式，
# 并返回一个可读性较好的字符串。

# 例如，考虑下面的示例代码：

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 25)
print(person) # Person(name=Alice, age=25)