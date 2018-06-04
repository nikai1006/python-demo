"""
函数返回值
每个函数绝对会有一个返回值（返回对象）
"""


def add(a, b):
    print(a, b)
    return  ##返回None


def add0(a, b):
    print(a, b)
    return None  ##同上


def add1(a, b):
    print(a, b)
    return a + b


result = add(2, 3)
print(result)
result = add0(3, 4)
print(result)
result = add1(1, 3)
print(result)
