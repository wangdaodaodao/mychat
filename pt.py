# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import json
import re
import os
import math
import PIL.Image as Image

 



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



