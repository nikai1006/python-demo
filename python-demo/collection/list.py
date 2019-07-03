#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : list.py
Author : nikai
Contect : TODO
Time : 2019/7/3 9:17
Desc : 
"""
if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
    list.append(100)
    print(list)
    print(list[-1])
    print(list[-5])
    list = range(1, 100, 2)
    print(list)
    print(list[-1])
    print(list[-20])
