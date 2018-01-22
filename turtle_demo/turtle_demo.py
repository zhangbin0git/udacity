#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2017/12/24 17:31 
# @Author : Mark 
# @Site :  home
# @File : turtle_demo.py 
# @Software: PyCharm Community Edition
import turtle

# 调用乌龟函数，画square
def draw_square(n):
    """画一个方形"""
    # 建立窗口
    window = turtle.Screen()
    # 窗口背景颜色
    window.bgcolor('red')

    # 画图
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(20)
    for i in range(0, n):
        print(i)
        brad.forward(100)
        brad.right(90)
        i += 1

    # 关闭窗口
    window.exitonclick()

draw_square(4)