#!/user/bin/env python
# coding=utf-8
"""
@project : yolov5
@author  : shanyi
#@file   : mv.py
#@ide    : PyCharm
#@time   : 2021-09-10 17:15:36
"""

from imutils.video import count_frames
import argparse
import os

# 构建命令行参数及解析
# -video 视频文件路径
# -override 是否使用手动计帧数
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
                help="path to input video file")
ap.add_argument("-o", "--override", type=int, default=-1,
                help="whether to force manual frame count")
args = vars(ap.parse_args())

# 计算视频文件的总帧数
override = False if args["override"] < 0 else True
total = count_frames(args["video"], override=override)

# 展示帧总数在终端上
print("[INFO] {:,} total frames read from {}".format(total,
                                                     args["video"][args["video"].rfind(os.path.sep) + 1:]))