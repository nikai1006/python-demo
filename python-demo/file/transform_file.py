#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name : transform_file.py
Author : nikai
Time : 2019/8/9 8:51
Desc : 
"""
import os
import shutil
import sys
import time


def copy(file, dest, min, subfix):
    """
    转换单个文件
    :param file:
    :param dest:
    :param min:
    :param subfix:
    :return:
    """
    if os.path.isfile(file):
        fpath, fname = os.path.split(file)
        if not os.path.exists(dest):
            os.makedirs(dest)
        if os.path.getsize(file) > min * 1024:
            shutil.move(file, dest + "/" + fname + subfix)
        else:
            print(file + " 小于" + str(min) + ",清理掉")
            os.remove(file)


def transform(path, dest="C://photo", min=20, subfix='.jpg'):
    """
    处理文件夹
    :param path:
    :param dest:
    :param min: 最小，默认20k
    :param subfix: 文件后缀
    :return:
    """
    if os.path.exists(path):
        if os.path.isdir(path):
            print(str(path))
            files = os.listdir(path)
            for file in files:
                path_file = path + "/" + file
                print("process " + file + ", " + str(os.path.getsize(path_file) / 1024) + "KB")
                copy(path_file, dest + "/" + time.strftime("%Y-%m-%d"), min, subfix)
        elif os.path.isfile(path):
            print(str(path) + "is file")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        transform(str(args[1]))
    else:
        print("请输入文件目录")
