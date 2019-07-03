#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : decorator.py
Author : nikai
Time : 2019/7/3 9:56
Desc : 修饰器
"""


def aDecorator(f):
    print("this is deaoctor")
    return f


@aDecorator
def a(x, y):
    print(x * y)


if __name__ == '__main__':
    a(4, 7)
    print(a.__name__)
