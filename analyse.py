# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'



import  json
import re
import os
import math

import PIL.Image as Image



def mergeImage():
    photo_width = 50
    photo_height = 50
    photo_path_list = []
    dirName = os.getcwd() + '/images'

    for root, dirs, files in os.walk(dirName):
        # print(root, dirs, files)
        for file in files:
            if 'jpg' in file and os.path.getsize(os.path.join(root, file)) > 0:
                photo_path_list.append(os.path.join(root, file))
            elif 'jpg' in file and os.path.getsize(os.path.join(root, file)) = 0:
                photo_path_list.append(os.path.join(root, file))





mergeImage()