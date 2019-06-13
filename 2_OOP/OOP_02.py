# 对象访问一个成员的时候，如果对象中没有该成员，尝试访问类中的同名成员。如果对象中有此成员，则一定使用此成员
class A():
    name = "wyb"
    age = 18

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
# 此时A称为类实例
print(A.name)
print(A.age)
# id可以鉴别一个变量是否和另一个变量是同一个变量
print(id(A.name))
print(id(A.age))
print("*" * 20)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))  # 打印出来的id竟然是一样的
'''上述案例说明：类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下。指向同一个变量。也就是对象属性
不赋值，那用的还是类里面的值'''
# 赋值对比一下，发现的确如此
a.name = "wyb2"
a.age = "22"
print(id(a.name))
print(id(a.age))

# self 本身不是一个关键字，作为一个参数传入
wyb = A()
wyb.say()
# self
class Teacher():
    name ="T"
    age = 33
    def say(self):
        self.name="Teacher"
        self.age= 90
        print("ok的")
    def sayAgain( ):
        print("Hello ")
        print( __class__.name )  # 调用类的成员变量需要使用 __class__

t = Teacher()
t.say()
Teacher.sayAgain() # 用类名可以调用，对比下面
# t.sayAgain() 报错的，因为没有self参数，对象是不可以访问这个方法的
# 报错内容 TypeError: sayAgain() takes 0 positional arguments but 1 was given
# 关于self的案例
print("self 案例")
class A():
    name = "WangYibo"
    age = 22
    def __init__(self): #构造函数
        self.name = "aaaa"
        self.age = 2333
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbbb"
    age = 90

a = A()
a.say() # 直接调，此时系统默认把a作为第一个参数传入函数
A.say(a) # 这样也可以，把a作为了一个参数进行传入
A.say(A) # 这样也可以。打印出来就不是say里面赋值的值了。 WangYibo 22
'''鸭子模型'''
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B) #bbbbb 90
'''鸭子模型'''

# 私有变量案例
class Person():
    # name 是共有成员
    name = "WangYibo"
    __age = 18

p =Person()
print(p.name)# 公有变量，可以访问
# 注意报错信息  AttributeError: 'Person' object has no attribute 'age'
#print(p.age) # age是私有变量，访问不了的
print(Person.__dict__)
print(p._Person__age)

