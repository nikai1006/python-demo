#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: slice.py
Author: nikai
Time: 2019/7/3 7:35
Desc: todo
"""
if __name__ == '__main__':
    list = [0, 1, 3, 4, 6]
    print(list[:3])
    print(list[2:4])
    print(list[-3:-1])
    print(list[3:])
    print(list[::2])
    print(list[3::2])
    name = "abcdefghigklmn"
    print(name[:8])
    print(name[8:])
    print(name[8:13])
    print(name[-8:])
    print(name[-8:-1])
    print(name[-8:-1:2])
    print(name[::3])
