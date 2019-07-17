# 继承的语法
# 在Python中，任何一个类都有一个共同的类object
class Person():
    name = "wyb"
    age = 18
    __score = 0 # 私有的
    _petname = "sec" # 小名，是傲虎的，子类可以用，不可以公用
    def sleep(self):
        print("Sleeping ....")
    def work(self):
        print("赚钱")
# 父类写在括号里面
class Teacher(Person):
    pass
    def makeTest(self):
        print("在考试")
    def work(self): #Person父类中存在work这个方法
        self.makeTest()    # 增加功能
        #扩充父类的功能只需要调用父类相同的函数
        Person.work(self)  # 方法1
        super().work()     # 方法2

t = Teacher()
print(t.name)  # 输出 ： wyb
print(t.makeTest())
# 受保护访问
print(t._petname)
# 私有访问
#print(t.__score) #'Teacher' object has no attribute '__score'


'''构造函数'''
class Dog():
    # __init__ 就是构造函数
    # 每次实例化的时候，第一个被调用
    # 主要工作室进行初始化
    def __init__(self):
        print("构造函数")

kaka = Dog()
'''继承中的构造函数'''
class Animal():
    pass

class PaxingAni(Animal):
    pass
    def __init__(self):
        print("爬行动物的构造函数")
    def __init__(self,name):  #构造函数含有参数
        print(name,"的构造函数")

class Cat(PaxingAni):
    def __init__(self):
        print("猫猫的构造函数")
# 此处不写构造函数
class ele(PaxingAni):
    pass
e = ele("wyb") # 那么调用的时候，ele里面没有构造函数，会去寻找父类里面的构造函数
