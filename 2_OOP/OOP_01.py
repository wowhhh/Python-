'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过，不用pass则会报错的
    pass

# 定义一个对象
wangyibo = Student()

#
class PythonStudent():
    name = None  # 姓名属性 ,用None占位，必须赋值的
    age = 18 # 值
    course = "Python"

# 注意
    # 1：缩进层级
    # 2：self
    def DoHomework(self): # 自动生成了self
        print("在做作业！")
        return None # 推荐在函数末尾使用return语句

wangyibo2 = PythonStudent()
wangyibo2.name = 'wyb'
print(wangyibo2.name)
wangyibo2.DoHomework()
PythonStudent.__dict__

# 对象访问一个成员的时候，如果对象中没有该成员，尝试访问类中的同名成员。如果对象中有此成员，则一定使用此成员
class A():
    name = "wyb"
    age = 18

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200

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