# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import json
import re
import os
import math

from pyecharts import Pie, Map, Bar, WordCloud
import codecs
from collections import Counter
import jieba.analyse
import PIL.Image as Image


from to_mongo import MongoPipeline


def dict2list(_dict):
    name_list = []
    num_list = []
    for k, v in _dict.items():
        name_list.append(k)
        num_list.append(v)
    return name_list, num_list

def counter2list(_counter):
    num_list = []
    name_list = []
    for item in _counter:
        name_list.append(item[0])
        num_list.append(item[1])
    return name_list, num_list

def get_pie(title, name_list, num_list):
    friend_nums = num_list[0] + num_list[1] + num_list[2]
    subtitle = '共有{}个好友'.format(friend_nums)

    pie = Pie(title, title_text_size=30, title_pos='center',
              subtitle=subtitle, subtitle_text_size=25, width=800, height=800)
    pie.add('', name_list, num_list, is_label_show=True, center=[50, 45], radius=[
            0, 50], legend='right', legend_orient='vertical', label_text_size=20)
    out_file_name = './analyse/{}.html'.format(title)
    pie.render(out_file_name)

def get_bar(title, name_list, num_list):
    bar = Bar(title, title_text_size=30, title_pos='center')
    bar.add('', name_list, num_list, title_pos='center', xaxis_interval=0, xaxis_rotate=27,
            xaxis_label_textcolor=20, yaxis_label_textcolor=20, yaxis_name_pos='end', yaxis_pos='%50')
    bar.show_config()
    # graph = Graph(width=1300, height=800)
    # graph.add(bar, graph_top='13%', graph_bottom='24%', graph_left='15%', graph_right='15%')
    out_file_name = './analyse/{}.html'.format(title)
    bar.render(out_file_name)

def get_map(title, name_list, num_list):
    _map = Map(title, width=1300, height=800, title_pos='center', title_text_size=30)
    _map.add('', name_list, num_list, maptype='china', is_visulamap=True, visual_text_color='#000')
    out_file_name = './analyse/{}.html'.format(title)
    _map.render(out_file_name)

def word_clout(title,name_list,num_list,word_size_range):
    '''词云图'''

    wordcloud = WordCloud(width=1400,height=900)

    wordcloud.add("",name_list,num_list,word_size_range=word_size_range,shape='pentagon')
    out_file_name = './analyse/'+title+'.html'
    wordcloud.render(out_file_name)
    
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
    toImage = Image.new(
        'RGBA', (photo_width * line_max, photo_height * row_max))

    for i in range(0, row_max):
        for j in range(0, line_max):
            pic_fole_head = Image.open(photo_path_list[num])
            tmppic = pic_fole_head.resize(
                (photo_width, photo_height),  Image.ANTIALIAS)
            print(j % line_max * photo_width,
                  row_max, photo_height, photo_width)
            loc = (int(j % line_max * photo_width),
                   int(i % row_max * photo_height))
            toImage.paste(tmppic, loc)
            num += 1
            if num >= len(photo_path_list):
                break
        if num >= pic_max:
            break
        print(toImage.size)
    toImage.save('{}/head_photo11.png'.format(dirName))


if __name__ == '__main__':

    # mongodb = db()
    # friends_info = mongodb.from_mongo()
    # mongodb.close_mongo()
    # frieds = list(friends_info)

    friends_file = './data/friends.json'
    with codecs.open(friends_file, encoding='utf-8') as f:
        friends = json.load(f)

    sex_counter = Counter()
    Province_counter = Counter()
    Signature_counter = Counter()
    NickName_list = []

    for friend in friends:
        sex_counter[friend['Sex']] += 1

        friend['Province'] = re.sub('[a-zA-Z]', '', friend['Province']).strip()
        if friend['Province'] != '':
            Province_counter[friend['Province']] += 1
            # if '山东' in friend['Province']:
            #     print(friend['NickName'])

    name_list, num_list = dict2list(sex_counter)
    get_pie('性别统计', name_list, num_list)


    name_list, num_list = counter2list(Province_counter.most_common(15))
    get_map('微信地区统计', name_list, num_list)
    get_bar('地区统计', name_list ,num_list)


    name_list,num_list = counter2list(Signature_counter.most_common(200))
    word_clout('微信好友签名关键字',name_list,num_list,[20,100])