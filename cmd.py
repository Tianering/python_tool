#!/user/bin/env python
# coding=utf-8
"""
@project : python_tool
@author  : shanyi
#@file   : cmd.py
#@ide    : PyCharm
#@time   : 2021-11-19 09:06:19
"""
import os
import csv

exe_path = "D:/DE_MX6600_20200807/cal_depth6600_1.exe"
ini_path = "D:/DE_MX6600_20200807/6600_config_copernicus.ini"
ref_path = "D:/IR/30/ir_ir27.000000_ldmp38.000000_0001.png"

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
        cmd = exe_path + " " + ref_path + " " + ini_path + " " + row[0]
        print(cmd)
        os.system(cmd)
