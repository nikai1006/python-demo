#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: lambda.py
Author: nikai
Time: 2019/7/3 23:40
Desc: 匿名函数 关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。

使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码：
"""
if __name__ == '__main__':
    a = map(lambda x: x * x, [i for i in range(1, 11)])
    print(list(a))
    for i in a:
        print(i)
