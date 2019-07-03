#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : set.py
Author : nikai
Time : 2019/7/3 9:22
Desc : 
"""
if __name__ == '__main__':
    myset = set([1, 2, 4, 4])
    print(myset)
    myset.add(3)
    print(myset)
    myset.add(3)
    myset.add(3)
    print(myset)
    myset.remove(4)
    print(myset)
    for i in myset:
        print(i)
