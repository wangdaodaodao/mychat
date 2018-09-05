# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import json
import re
import os
import math

from pyecharts import Bar,Grid, Word
from collections import Counter
import jieba.analyse
import PIL.Image as Image

from to_mongo import MongoPipeline

def get_pie(title, name_list, num_list):
    pass

def mergeImage():
    photo_width = 50
    photo_height = 50
    photo_path_list = []
    dirName = os.getcwd() + '/images'

    for root, dirs, files in os.walk(dirName):
        for file in files:
            if 'jpg' in file and os.path.getsize(os.path.join(root, file)) > 0:
                photo_path_list.append(os.path.join(root, file))
            elif 'jpg' in file and os.path.getsize(os.path.join(root, file)) == 0:
                photo_path_list.append(os.path.join(root, file))

    pic_num = len(photo_path_list)
    line_max = int(math.sqrt(pic_num)) - 2
    row_max = int(math.sqrt(pic_num)) + 4
    print(line_max, row_max, pic_num)

    if line_max > 20:
        line_max = 20
        row_max = 20

    num = 0
    pic_max = line_max * row_max
    toImage = Image.new('RGBA', (photo_width * line_max, photo_height * row_max))

    for i in range(0, row_max):
        for j in range(0, line_max):
            pic_fole_head = Image.open(photo_path_list[num])
            tmppic = pic_fole_head.resize((photo_width, photo_height),  Image.ANTIALIAS)
            print(j % line_max * photo_width, row_max, photo_height, photo_width)
            loc = (int(j % line_max * photo_width),int(i % row_max * photo_height))
            toImage.paste(tmppic, loc)
            num += 1
            if num >= len(photo_path_list):
                break
        if num >= pic_max:
            break
        print(toImage.size)
    toImage.save('{}/head_photo11.png'.format(dirName))


...
def make_photo():
        dirName = os.getcwd() + '/images'
        dirName2 =  os.getcwd() + '/images2'
        for root, dirs, files in os.walk(dirName):
            #遍历文件
            for file in files:
                file_dir = '{}/{}'.format(root, file)
                print(file_dir)
                img = Image.open(file_dir)
                width, height = img.size
                #裁剪区域
                region=(0,500,700,1100)
                cropimg = img.crop(region)
                print(cropimg.size)
                #同比例缩放,注意images.ANTIALIAS参数
                img2 = cropimg.resize((100, 100), Image.ANTIALIAS)
                print(img2.size)
                img2.save('{}/{}'.format(dirName2, file))


...

