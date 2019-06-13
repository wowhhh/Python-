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

