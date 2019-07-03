#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : tuple.py
Author : nikai
Time : 2019/7/3 9:24
Desc : 
"""
if __name__ == '__main__':
    t = (1,)
    print(t)
    t = (1, [2, 3])
    print(t)
    t[1][1] = 5
    print(t)
    for i in t:
        print(i)
