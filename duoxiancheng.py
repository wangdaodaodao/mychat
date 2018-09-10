#_*_ coding:utf-8 _*_

import os
import requests
import time

from lxml import etree

keyword = input('输入关键词：')

class Spider():
    def __init__(self):
        self.headers = {
            'User-Agnet': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
        }
        self.filepath = '/{}/'.format(keyword)
    
    def creat_file(self):
        filepath = self.filepath
        if not os.path.exists(filepath):
            os.makedirs(filepath)
    
    def get_pagenum(self):
        total = ''
        url ='https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc'.format(keyword)
        html = requests.get(url, headers = self.headers)
        selector = etree.HTML(html.text)
        pageinfo = selector.xpath('//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageinfo[0])
        numlist = list(filter(str.isdigit, string))
        for item in numlist:
            total += item
            totalpagenum = int(total)
        return totalpagenum
