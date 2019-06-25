# 继承的语法
# 在Python中，任何一个类都有一个共同的类object
class Person():
    name = "wyb"
    age = 18
    __score = 0 # 私有的
    _petname = "sec" # 小名，是傲虎的，子类可以用，不可以公用
    def sleep(self):
        print("Sleeping ....")

# 父类写在括号里面
class Teacher(Person):
    pass
    def makeTest(self):
        print("在考试")


t = Teacher()
print(t.name)  # 输出 ： wyb
print(t.makeTest())
# 受保护访问
print(t._petname)
# 私有访问
print(t.__score) #'Teacher' object has no attribute '__score'