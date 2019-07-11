# 属性案例
# 创建Student类，描述学生类
# 学生具有student.name属性
# 但是name格式并不统一，可以增加一个函数，使不同的格式统一化
'''本函数目的：名字大写'''
class Student():
    name = ""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 调用自身的函数
        self.setName(name)
    #自定义函数：介绍一下自己
    def intro(self):
        print("Hi,My name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper() # .upper() 变成大写

s1 = Student("Wang  Yibi",19)
s2 = Student("michi stangle"  ,24)
s1.intro()
s2.intro()
'''本函数目的：名字大写'''

# property案例
#定义一个person类，具有name,age属性
#对于任意输入的姓名，都以为是大写方式保存
#对于任意输入的年龄，统一使用整数保存
class Person():
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2
    def fset(self,name): # RecursionError: maximum recursion depth exceeded while calling a Python object
        # 输入姓名大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = "NoName"
    name = property(fget,fset,fdel,"doc函数是说明文档")
p1 = Person()
p1.name = "Wang Yibo"
print(p1.name)  # 输出结果：WANG YIBOWANG YIBO

'''作业：
1：在用户输入年龄的时候，可以输入整数、小数、浮点数
2：但内部为了数据清洁，我们统一需要保存整数，直接舍去小数点
'''
class Person2():
    def fget(self):
        return self._age
    def fset(self,age):
        self._age = int(age)
    def fdel(self):
        self._age = 0
    age = property(fget,fset,fdel,"设置年龄")
p2 = Person2()
p2.age = 18.8
print(p2.age)

'''
类的内置属性
'''
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)