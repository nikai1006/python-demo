#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : params_decorator.py
Author : nikai
Contect : TODO
Time : 2019/7/4 8:29
Desc :带参数修饰器
"""
import time,functools


def pDecorator(level):
    def inner_decorator(f):
        @functools.wraps(f) #复制原来的函数属性到现在的函数上面
        def wrapper(*args, **kwargs):
            print("[%s] call %s on %s" % (level, f.__name__, time.time()))
            return f(*args, **kwargs)

        return wrapper

    return inner_decorator


@pDecorator(level='INFO')
def a(x):
    return x * x


if __name__ == '__main__':
    print(a(3))
    print(a.__name__)
