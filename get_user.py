# -*- conding:utf-8 -*-
__author__ = 'wangdaodao'


import json

import itchat
import codecs

# from to_mongo import MongoPipeline as db

def save_to_file(friends_list):
    out_file = './data/friends.json'
    with codecs.open(out_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(friends_list, ensure_ascii=False))


# def save_to_mongo(friends_list):
    # mongodb = db()
    # mongodb.to_mongo(friends_list)

def download_images(friends_list):
    imamge_dir = './imagers/'
    num = 1
    for f in friends_list:
        image_name = str(num) + '.jpg'
        num += 1
        img = itchat.get_head_img(userName=f['UserName'])
        with open(imamge_dir + image_name, 'wb') as ff:
            ff.write(img)



if __name__ == '__main__':
    itchat.login()
    friends = itchat.get_friends(update=True)[0: 5]
    friends_list = []

    sex_dict = {}
    sex_dict['0'] = '其他'
    sex_dict['1'] = '男'
    sex_dict['2'] = '女'

    for friend in friends:
        item = {}
        item['NickName'] = friend['NickName']

        item = {}
        item['NickName'] = friend['NickName']
        item['HeadImgUrl'] = friend['HeadImgUrl']
        item['Sex'] = sex_dict[str(friend['Sex'])]
        item['Province'] = friend['Province']
        item['City'] = friend['City']
        item['Signature'] = friend['Signature']
        item['UserName'] = friend['UserName']

        # 保存到mongo
        # save_to_mongodb(item)
        friends_list.append(item)



save_to_file(friends_list)