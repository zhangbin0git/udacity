#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2017/12/24 10:59 
# @Author : Mark 
# @Site : home
# @File : Private_information.py 
# @Software: PyCharm Community Edition

import os
def rename_files():
    # get filename
    path_pic = 'D:/udacity/Private_information/pic'
    file_name = os.listdir(path_pic)
    # rename filename
    print('当前文件path:' + os.getcwd())
    path = 'D:/udacity/Private_information/pic'
    os.chdir(path)
    print('当前文件path:' + os.getcwd())
    print('--------------------------------------------------------')
    for name in file_name:
        print('之前的名字：' + name)
        new_name = name.translate(name.maketrans('', '', '1234567890'))
        os.rename(name, new_name)
        print('修改之后的名字：' + new_name)

# 运行
rename_files()
