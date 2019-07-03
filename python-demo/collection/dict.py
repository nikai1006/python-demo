#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : dict.py
Author : nikai
Time : 2019/7/3 9:27
Desc : 
"""
if __name__ == '__main__':
    user = {
        'name': 'lucy',
        'age': 3,
        'sex': 'women',
        'student': False
    }
    user['dad'] = 'nikai'
    user.setdefault('mom', 'nacy')
    print(user['name'])
    print(user.get('name'))
    print('---------------------------------------------')
    for key, value in user.items():
        print(key, value)
    print('---------------------------------------------')
    for value in user.values():
        print(value)
    print('---------------------------------------------')
    for i in user:
        print(i)
