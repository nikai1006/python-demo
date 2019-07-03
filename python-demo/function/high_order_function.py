#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : high_order_function.py
Author : nikai
Time : 2019/7/3 9:48
Desc : 高阶函数
"""


def a(f):
    result = f(10)
    return result


def b(x):
    return x * x


def c(y):
    return y + 10


def d(f):
    print(f(10))

    def e(x, y):
        return x * y

    return e


if __name__ == '__main__':
    print(a(b))
    print(a(c))
    e = d(b)
    print(e(2, 5))
    print(d(c)(3, 4))
