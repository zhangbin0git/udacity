#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/1/11 21:56 
# @Author : Mark 
# @Site :  office
# @File : jwjc_demo.py 
# @Software: PyCharm Community Edition
# 利用之前现场存储下的数据模拟检查汽车的运行
import time
import pyodbc
def data_demo():
    """测试实时数据"""

    transition_data = []
    with open('date.csv', 'r') as file:
        # 跳过文件的第一行
        next(file)
        # 读取所有行
        line = file.readlines()
        for data in line:
            # 去掉每行的两边的空白数据
            data = data.strip()
            # 更加','建立数据
            transition_data = data.split(',')
            # 更新插入时间
            input_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 将写入时间设为插入时间 transition_data[2] 为DDatetime
            transition_data[2] = input_time
            # transition_data[10] 为InputDateTime
            transition_data[10] = input_time
            # 将每条数据每隔5s写入数据库
            time.sleep(0.01)
            print(transition_data)
            insert_sql(transition_data)

def insert_sql(array=[]):
    """写入数据"""
    # 链接数据库
    conn = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 10.0};SERVER=127.0.0.1,1433;'
        r'DATABASE=zkhy_vmld_01;UID=sa;PWD=12345678')
    # 建立链接
    cursor = conn.cursor()
    # 生成insert语句
    values = "insert into VRealDataTable(VCode, DDateTime, ENumber,CValue, " \
             "LStrength, Longitude, Latitude, SCount, VSpeed, InputDateTime) " \
             "values("
    # 将传入的数字放入插入语句
    for array_str in array[1:-1]:
        values += "'" + array_str + "', "
    values = values + "'" + array[-1] + "')"
    # 插入数据
    cursor.execute(values)
    #提交
    conn.commit()

if __name__ == '__main__':
    data_demo()
    # input("Enter the any press to exit")
