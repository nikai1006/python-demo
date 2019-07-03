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
    lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
    lt.append(100)
    print(lt)
    print(lt[-1])
    print(lt[-5])
    lt = [i for i in range(1, 100, 2)]
    print(lt)
    print(lt[-1])
    print(lt[-20])
    # 字符串转list
    lt = list("abcdefghijklmnopqrst")
    print(lt)
    # list转字符串
    words = ''.join(lt)
    print(type(words))
    print(words)
    # 元组转list
    lt = list((1, 2))
    print(lt)
