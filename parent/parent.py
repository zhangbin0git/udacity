#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2017/12/25 0:07 
# @Author : Mark 
# @Site : home
# @File : parent.py 
# @Software: PyCharm Community Edition
# 继承

class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent 输出')
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print('Child 输出')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


man = Parent('zhangbin', 'black')

duo = Child('zhanglinxi', 'black', '10')

print(man.last_name)
print(duo.last_name)


