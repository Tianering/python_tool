#!/user/bin/env python
# coding=utf-8
"""
@project : TemperatureCompensation
@author  : shanyi
#@file   : traverse.py
#@ide    : PyCharm
#@time   : 2021-11-18 16:38:37
"""
import os
import csv

dir_path = "/home/shanyi/data/temp_826_b/IR"
dir_list = os.listdir(dir_path)
f = open('/home/shanyi/data/temp_826_b/filelist.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
for dir in dir_list:
    temper_dir = os.path.join(dir_path, dir)
    for file in os.listdir(temper_dir):
        if file.endswith(".png"):
            if not file.startswith("ud_"):
                csv_writer.writerow([os.path.join(temper_dir, file)])
                print(os.path.join(temper_dir, file))
