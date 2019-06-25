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