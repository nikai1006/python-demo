#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : muliti_loop.py
Author : nikai
Time : 2019/7/3 9:39
Desc : 多重循环
"""
if __name__ == '__main__':
    list = [m + n for m in 'ABC' for n in '123']
    print(list)
