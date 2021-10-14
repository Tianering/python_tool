#!/user/bin/env python
# coding=utf-8
"""
@project : SML
@author  : shanyi
#@file   : xmls_ed.py
#@ide    : PyCharm
#@time   : 2021-09-17 15:29:48
"""
import os
import xml.dom.minidom
import xml.etree.ElementTree

xmldir = '/home/shanyi/data/VOC2012/Annotations/'  # 你的xml文件的路經，注意最后一定要有'/'

for xmlfile in os.listdir(xmldir):
    xmlname = os.path.splitext(xmlfile)[0]

    # 读取 xml 文件
    dom = xml.dom.minidom.parse(os.path.join(xmldir, xmlfile))
    root = dom.documentElement

    # 获取标签对的名字，并为其赋一个新值
    # root.getElementsByTagName('folder')[0].firstChild.data = 'nano_coco'
    # root.getElementsByTagName('filename')[0].firstChild.data = xmlname + '.png'
    # root.getElementsByTagName('path')[0].firstChild.data = \
    #     '/home/shanyi/data/nano_coco/val/' + xmlname + '.png'
    # root.getElementsByTagName('width')[0].firstChild.data = '2084'
    # root.getElementsByTagName('height')[0].firstChild.data = '2084'

    if int(root.getElementsByTagName('xmax')[0].firstChild.data) > 320:
        root.getElementsByTagName('xmax').firstChild.data = 320

    # 修改并保存文件
    xml_specific = xmldir + xmlfile
    with open(xml_specific, 'w') as fh:
        dom.writexml(fh)
