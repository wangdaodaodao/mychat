# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import json
import re
import os
import math

<<<<<<< HEAD
from pyecharts import Bar, Grid, WordCloud, Pie, Map
from collections import Counter
=======
from pyecharts import Bar,Grid, Word
from collections import Counter
import jieba.analyse
>>>>>>> 21c16047507fea056843ba45e268621409a401b9
import PIL.Image as Image
import codecs

from to_mongo import MongoPipeline

<<<<<<< HEAD
def get_pie(title, name_list, num_list):
    friend_nums = num_list[0] + num_list[1] + num_list[2]
    subtitle = '共有：{}个好友'.format(friend_nums)
    pie = Pie(title, page_title)
=======
from to_mongo import MongoPipeline

def get_pie(title, name_list, num_list):
    pass
>>>>>>> 21c16047507fea056843ba45e268621409a401b9

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




