"""
可变参数函数
变长参数会自动转变为以参数名命名的元组或字典
"""


def add(*args):
    print(args)  ##元组
    print(args.__class__)
    for arg in args:
        print(arg)


add(3, 4, 5, 6, 7)

add(2, 5)


def welcom(**kwargs):  ###字典
    print(kwargs)
    print(kwargs.__class__)


welcom(name='lucy', age=33, sex='f')
