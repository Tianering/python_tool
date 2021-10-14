#!/user/bin/env python
# coding=utf-8
"""
@project : SML
@author  : shanyi
#@file   : asc_ed.py
#@ide    : PyCharm
#@time   : 2021-10-14 11:54:29
"""
# 读取并修改asc文件
import pandas as pd
import os

if __name__ == '__main__':

    path = '/home/shanyi/data/asc/'
    # 获取该目录下所有文件，存入列表中
    fileList = os.listdir(path)
    for i in fileList:
        if i.endswith(".asc"):
            filepath = path + os.sep + i
            ASCfile = pd.read_csv(filepath, skiprows=0, encoding="gbk", engine='python', sep=' ', delimiter=None,
                                  index_col=False, header=None, skipinitialspace=True)
            # print(ASCfile.columns)
            # print(ASCfile.iloc[0:, 1:4])  # 行，列 = [:, :]
            # print(ASCfile)
            ASCfile = ASCfile.iloc[0:, 1:4]
            ASCfile.to_csv(path + os.sep + "ed/" + i, index=False, header=False, sep=' ')
