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
print(Person.__bases__) # (<class 'object'>,)

'''
init举例
'''
class A():
    def __init__(self, name = 0):
        print('ok')
    def  __call__(self):
        print("call 函数调用")
    def __str__(self):
        return "str函数调用"
a = A() #此处调用构造函数

'''
call 举例
'''
a() # 当A类中没有call函数却把a对象当作函数来使用的时候 此处会出现问题， TypeError: 'A' object is not callable
# 解决方法就是在A类里面添加call函数

'''
str 举例
'''
print(a) # 直接如此打印 <__main__.A object at 0x000002D198950F60>
# 但是在A类里面加入__str__函数之后，就会打印出函数return的内容

'''
__getattr__
'''
class B():
    name = "noname"
    age = 18
    def __getattr__(self,item):
        print("没找到此属性")
b = B()
print(b.name)
print(b.noattr)#如果类里面没有__getattr__函数，那么会报错print(b.noattr) # 'B' object has no attribute 'noattr'
# 但是存在__getattr__函数的时候，就会调用此类里面的这个函数,然后这个print(bb.noattr)还是None

'''
__setattr__
'''
class C():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("{0}设置成功".format(name))
        #下面语句会导致死循环
        # self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)
c = C()
print(c.__dict__) # 打印所有函数： {}
c.age = 18 # 打印结果：age设置成功

'''
__gt__ 案例
'''
class S():
    def __init__(self,name):
        self._name = name


    def __gt__(self, obj):
        print("h,{0} 会比 {1} 大么？".format(self, obj))
        return self._name > obj._name


s1 = S('wyb')
s2 = S('wyb2')
print(s1>s2) # 如果没有函数__gt__，出错：TypeError: '>' not supported between instances of 'S' and 'S'
# 即对象之间没办法比较，但是有了__gt__函数，就可以进行函数内要求的比较行为。

'''
类和对象的三种方法
'''
class person6:
    # 实例方法
    def eat(self):
        print(self)
        print('吃')
    # 类方法
    # 第一个参数一般命名为cls,区别与self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing....')

    #静态方法
    # 不需要第一个参数表示自身或者类
    @staticmethod
    def say():
        print("shuo....")

one1 = person6()
#实例方法
one1.eat()
# 类方法
person6.play()
one1.play() #也可以
#静态方法
person6.say()
one1.say() #也可以