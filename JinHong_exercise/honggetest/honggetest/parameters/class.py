#定义类
# class classname:
#     i = 123
#     def f(self):
#         return "hello world"
# print(classname.i)
# classname.i = 10
# q = classname
# print(q.i)
#
#

# class complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = complex(3.0, 4.5)
# print(x.r)
# print(x.i)
# class Employee:
#     empCount = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1

#
# class parent:
#     def mymethod(self):
#         print("调用父类方法")
#
# class child(parent):
#     def mymethod(self):
#         print("调用子类方法")
# c = child()
# c.mymethod()
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
b = Bag()
print(b.data)
b.add("1")
print(b.data)
b.addtwice("x")
print(b.data)


class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__updata(iterable)
    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)
#自定义一个类student
class student():
    def speak(self):
        print("%s 说：我今年%s岁" % (self.name, self.age))# 哪个对象调用了这个方法，self就是那个对象；可以把self理解为一个形参
#类student 实例化一个对象john
john = student()
# 给对象添加属性
john.name = "约翰"
john.age = 19
# 调用类中的 speak()方法
john.speak()

class student(object):
    # 定义构造方法
    def __init__(self, n, a):  #__init__() 是类的初始化方法；它在类的实例化操作后 会自动调用，不需要手动调用；
        self.name = n
        self.age = a
# 定义普通方法
    def speak(self):
        print("%s 说：我今年%s岁" % (self.name, self.age))
#类student 实例化一个对象john
john = student("约翰",19)
# 调用类中的 speak()方法
john.speak()













