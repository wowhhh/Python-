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
'''上述案例说明：类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下。指向同一个变量。也就是对象属性
不赋值，那用的还是类里面的值'''