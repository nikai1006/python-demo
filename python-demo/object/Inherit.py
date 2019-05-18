"""
Python 继承
"""

class A(object):
    def doSomething(self):
        print('this is A')


class B(A):

    def doSomething(self):
        print("this is B")
        super(B, self).doSomething()


if __name__ == '__main__':
    b = B()
    b.doSomething()
