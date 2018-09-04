# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import os
import PIL.Image as Image


def make_photo():
    '''
    遍历文件，裁剪，缩小
    '''
    dir_name = os.getcwd() + '/images'
    dir_name2 = os.getcwd() + '/images2'
    for root, dirs, files in os.walk(dir_name):
        # 遍历文件
        print(dirs)
        for file in files:
            file_dir = '{}/{}'.format(root, file)
            print(file_dir)
            img = Image.open(file_dir)
            # 裁剪区域
            region = (0, 500, 700, 1100)
            cropimg = img.crop(region)
            print(cropimg.size)
            # 同比例缩放,注意images.ANTIALIAS参数
            img2 = cropimg.resize((100, 100), Image.ANTIALIAS)
            print(img2.size)
            img2.save('{}/{}'.format(dir_name2, file))

make_photo()
