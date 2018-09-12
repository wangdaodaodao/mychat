#_*_ coding:utf-8 _*_

import os
import requests
import time
from threading import Thread
from lxml import etree

keyword = input('输入关键词：')
if len(keyword) < 2:
    keyword = '美女'


class Spider():
    def __init__(self):
        self.headers = {
            'User-Agnet': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
        }
        self.filepath = './{}/'.format(keyword)

    def creat_file(self):
        filepath = self.filepath
        if not os.path.exists(filepath):
            os.makedirs(filepath)

    def get_pagenum(self):
        total = ''
        url = 'https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc'.format(
            keyword)

        html = requests.get(url, headers=self.headers)
        selector = etree.HTML(html.text)
        pageinfo = selector.xpath(
            '//header[@class="listing-header"]/h1[1]/text()')
        string = str(pageinfo[0])
        numlist = list(filter(str.isdigit, string))
        for item in numlist:
            total += item
            totalpagenum = int(total)
        return totalpagenum

    def get_links(self, number):
        url = "https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&sorting=relevance&order=desc&page={}".format(
            keyword, number)
        try:
            html = requests.get(url, headers=self.headers)
            selector = etree.HTML(html.text)
            pic_linklist = selector.xpath(
                '//a[@class="jsAnchor thumb-tags-toggle tagged"]/@href')
            return pic_linklist
        except Exception as e:
            print(e)


    def download(self, url, count):
        string = url.strip(
            '/thumbTags').strip('https://alpha.wallhaven.cc/wallpaper/')
        html = 'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-' + string + '.jpg'
        pic_path = '{}/{}-{}.jpg'.format(self.filepath, count, str(string))
        if os.path.exists(pic_path):
            print('文件已存在！')
        else:
            try:
                start = time.time()
                pic = requests.get(html, headers=self.headers)
                with open(pic_path, 'wb') as code:
                    code.write(pic.content)
                end = time.time()
                print('正在下载图片{}，单个文件耗时：{}s'.format(string,(end - start)))
            except Exception as e:
                print(e)

    def main_function(self):
        self.creat_file()
        count = self.get_pagenum()
        times = int(count / 24 + 1)
        j = 1
        start1 = time.time()
        for j in range(times):
            pic_urls = self.get_links(j)
            threads = []
            for item in pic_urls:
                start2 = time.time()
                t = Thread(target=self.download, args=[item, j])
                t.start()
                threads.append(t)
                end2= time.time()
                j += 1
            print('第{}页下载完毕！'.format(j))
            for t in threads:
                t.join()
        end1 = time.time()
        print('总耗时：{}'.format(end1 - start1))


spider = Spider()
spider.main_function()
