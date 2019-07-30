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
import math
import re

import requests
from bs4 import BeautifulSoup

from project.plugin.log_tool import LogTool

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
    pl_url= 'https://api.bilibili.com/x/v2/reply'

    def __init__(self):
        # 视频av
        self.av = None
        # 获取弹幕数据的cid
        self.cid = None
        # 弹幕数据
        self.items = None
        # name解析
        self.names = None

    def run(self):
        self.av = str(61076937)

        self.get_aid()
        # self.get_dm()
        self.get_pl()
        self.write_dm_to_json()

    # 获取aid
    def get_aid(self):
        LogTool.print("---------获取aid----------")
        url = self.main_url_pattern.format(av=self.av)
        res = self.get_response(url)
        self.cid = str(re.findall('"cid=(\d+)&aid=\d+&', res.text)[0])
        print(self.cid)

    def get_pl(self):
        ret = self.get_pl_numb()
        LogTool.print(f"评论总页面：{ret}")
        pass

    def get_pl_numb(self):
        video_url_params = {
            'jsonp': 'jsonp',
            'pn': '1',  # 页数
            'type': '1',
            'oid': self.av,  # 视频id
            'sort': '0',
        }
        ret = requests.get(self.pl_url, params=video_url_params,
                               headers=headers).json()
        data = ret['data']
        # 获得总评论数
        pages_number = data['page']['count']
        for replie in data['replies']:
            # 循环获得次视频下面的评论
            neirong = replie['content']['message']
            pass
        # 获得并返回页数，每页有20条评论，所以返回总页数除20并且向上取整
        return math.ceil(pages_number / 20)

    # def get_pl_list(self):
    #     Get_list_params = {
    #         'mid': UP_main_ID,  # 设置up主ID
    #         'pagesize': '30',
    #         'tid': '0',
    #         'page': Page,  # 第几页
    #         'keyword': '',
    #         'order': 'pubdate',
    #     }








    # 获取弹幕json数据
    def get_dm(self):
        LogTool.print("---------获取json----------")
        dm_url = self.dm_url_pattern.format(cid=self.cid)
        # print(dm_url)
        soup = self.get_soup(dm_url)
        ds = soup.select('d')
        items = []
        for d in ds:
            item = self.hash_get_id(d.get('p'), d.text)
            LogTool.print(item)
            items.append(item)
        # 保存弹幕数据
        self.items = items

    #弹幕json数据写入文本
    def write_dm_to_json(self):
        with open(str(self.av) + '.json', 'w', encoding='utf8') as f:
            json.dump(self.items, f)

    # hash解析单个id
    def hash_get_id(self, p, text):
        item = {}
        hash_id = re.findall(r',0,(.*?),', p)[0]
        # print(hash_id)
        hash_url = self.hash_url_pattern + str(hash_id)
        res = self.get_response(hash_url).json()
        # id = ""
        if res['error'] == 0:
            id = res['data'][0]['id']
            name, description, face = self.id_get_name(id)
            return {"text":text, "id": id, "name": name, "description": description, "face": face}
        return {}

    # 由id获取用户名
    def id_get_name(self, id):
        data = {'mid': id}
        res = requests.post(url=self.Infou, headers=headers, data=data)
        dic = res.json()
        return dic['data']['name'], dic['data']['sign'], dic['data']['face']
        # for item in self.items:
        #     if item['id']:
        #         data = {'mid': item['id']}
        #         res = requests.post(url=self.Infou, headers=headers, data=data)
        #         print(res.json())
        #         dic = res.json()
        #         item['name'] = dic['data']['name']
        #         item['description'] = dic['data']['sign']
        #         item['face'] = dic['data']['face']
        #         print(item)
        #     else:
        #         item['name'], item['description'], item['face'] = None, None, None

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
