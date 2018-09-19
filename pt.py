# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import os
import math
import PIL.Image as Image


photo_height = 50
photo_width = 50
photo_dir = []


def make_photo():
    '''
    遍历文件，裁剪，缩小
    '''
    dir_name = os.getcwd() + '/images'
    dir_name2 = os.getcwd() + '/images2'

    for root, dirs, files in os.walk(dir_name):
        pic_num = len(files)

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
            img2 = cropimg.resize((photo_height, photo_width), Image.ANTIALIAS)
            print(img2.size)
            img2.save('{}/{}'.format(dir_name2, file))
            photo_dir.append(file)

    line_max = int(math.sqrt(pic_num))
    row_max = int(math.sqrt(pic_num))
    print(line_max, row_max, pic_num)
    print(photo_dir)

    if line_max > 10:
        line_max = 10
        row_max = 10

    num = 0
    pic_max = line_max * row_max
    toImage = Image.new(
        'RGBA', (photo_width * line_max, photo_height * row_max))

    for i in range(0, row_max):
        for j in range(0, line_max):
            pic_fole_head = Image.open(
                '{}/{}'.format(dir_name2, photo_dir[num]))
            tmppic = pic_fole_head.resize(
                (photo_width, photo_height), Image.ANTIALIAS)
            loc = (int(j % line_max * photo_width),
                   int(i % row_max * photo_height))
            toImage.paste(tmppic, loc)
            num += 1
            if num >= len(photo_dir):
                break
        if num >= pic_max:
            break
        print(toImage.size)

    toImage.save('head_photo11.png')
