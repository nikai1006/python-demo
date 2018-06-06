"""
class示例

class 类名:
    .....
    def 方法名(self,参数列表):
        ....


#实例化方法的调用
实例名.方法名
"""


class Person:
    def eat(self, food):
        print("person eat " + str(food))


man = Person()  ##实例化类
man.eat('banana')
