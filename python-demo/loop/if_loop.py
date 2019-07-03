#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : if_loop.py
Author : nikai
Time : 2019/7/3 9:36
Desc : 带有判断的循环
"""
if __name__ == '__main__':
    list = [x * x for x in range(1, 11)]
    print(list)
    list = [x * x for x in range(1, 11) if x % 2 == 0]
    print(list)
