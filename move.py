#!/user/bin/env python
# coding=utf-8
"""
@project : python_tool
@author  : shanyi
#@file   : move.py
#@ide    : PyCharm
#@time   : 2021-11-19 09:29:18
"""
import os
import shutil

dir_path = "/home/data/temp_826_b/IR/"
dir_list = os.listdir(dir_path)
strs = ["disp", "depth", "point"]
for str in strs:
    for dir in dir_list:
        temper_dir = os.path.join(dir_path, dir)
        if os.path.isdir(dir):
            for file in os.listdir(temper_dir):
                file_path = os.path.join(temper_dir, file)
                temp_path = os.path.join(temper_dir, str)
                new_path = os.path.join(temp_path, file)
                if os.path.isfile(file_path):
                    if str in file:
                        shutil.move(file_path, new_path)
