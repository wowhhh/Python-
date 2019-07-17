'''super 和 mro
可以把mro理解成家谱
'''
class A():
    pass
class B(A):
    pass

class C(B,A):
    pass
print(A.__mro__) #(<class '__main__.A'>, <class 'object'>)
print(B.__mro__) #(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("游泳ing")

class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("飞ing")

class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("干活ing")

class SuperMan(Person,Bird,Fish):
    pass

s  = SuperMan("wyb")
s.fly()
s.swim()
s.work()