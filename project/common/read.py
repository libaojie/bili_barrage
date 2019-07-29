#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2019/7/22 19:53
@Author     : libaojie
@File       : read.py
@Software   : PyCharm
"""

import json
import re
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/60.0.3112.101 Safari/537.36',
           'Referer': 'http://space.bilibili.com/43085921'}


class Read(object):
    main_url_pattern = 'https://www.bilibili.com/video/av{av}/'
    dm_url_pattern = 'http://comment.bilibili.com/{cid}.xml'
    hash_url_pattern = 'http://biliquery.typcn.com/api/user/hash/'
    space_url_pattern = 'https://space.bilibili.com/{av}'
    Infou = 'https://space.bilibili.com/ajax/member/GetInfo'

    def __init__(self, av):
        # 视频av
        self.av = str(av)
        # 获取弹幕数据的cid
        self.cid = None
        # 弹幕数据
        self.items = None
        # name解析
        self.names = None

    # 获取aid
    def get_aid(self):
        url = self.main_url_pattern.format(av=self.av)
        res = self.get_response(url)
        self.cid = str(re.findall('"cid=(\d+)&aid=\d+&', res.text)[0])
        print(self.cid)

    # 获取弹幕json数据
    def get_dm(self):
        dm_url = self.dm_url_pattern.format(cid=self.cid)
        print(dm_url)
        soup = self.get_soup(dm_url)
        ds = soup.select('d')
        items = []
        for d in ds:
            # print(d.get('p'), d.text)
            item = {
                'p': d.get('p'),
                'content': d.text
            }
            items.append(item)
        # 保存弹幕数据
        self.items = items
        # self.write_dm_to_json()

    # 弹幕json数据写入文本
    def write_dm_to_json(self):
        with open(str(self.av) + '.json', 'w', encoding='utf8') as f:
            json.dump(self.items, f)

    # hash解析获得全部id
    def hash_get_all_id(self):
        for item in self.items:
            self.hash_get_id(item)

    # hash解析单个id
    def hash_get_id(self, item):
        hash_id = re.findall(r',0,(.*?),', item['p'])[0]
        # print(hash_id)
        hash_url = self.hash_url_pattern + str(hash_id)
        res = self.get_response(hash_url).json()
        if res['error'] == 0:
            item['id'] = res['data'][0]['id']
        else:
            item['id'] = None
        print(item)

    # 由id获取用户名
    def id_get_name(self):
        for item in self.items:
            if item['id']:
                data = {'mid': item['id']}
                res = requests.post(url=self.Infou, headers=headers, data=data)
                print(res.json())
                dic = res.json()
                item['name'] = dic['data']['name']
                item['description'] = dic['data']['sign']
                item['face'] = dic['data']['face']
                print(item)
            else:
                item['name'], item['description'], item['face'] = None, None, None

    # 保存到mongo
    def save_to_mongo(self):
        for item in self.items:
            # self.db[MONGO_TABLE].insert(item)
            print(item)

    # 利用requests.get()方法获得sponse对象('utf8')
    @staticmethod
    def get_response(url, headers=headers):
        try:
            response = requests.get(url, headers=headers)
            response.encoding = 'utf8'
            if response:
                return response
        except Exception as e:
            print(e)

    # 利用BeautifulSoup库返回soup对象
    def get_soup(self, url, headers=headers):
        response = self.get_response(url, headers)
        if response:
            soup = BeautifulSoup(response.text, 'lxml')
            return soup
