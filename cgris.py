#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:joel 18-6-5

import random
import time
import requests
import math
import pymongo
import socket
socket.setdefaulttimeout(20)

postUrl = 'http://www.cgris.net/query/o.php'
user_agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
]
headers = {
    'User-Agent':user_agent[random.randint(0,20)],
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest'
}

start_url = 'http://www.cgris.net/query/o.php'

proxies = [
    {'https': '118.190.145.138:9001'},
    {'https': '106.8.17.23:60443'},
    {'https': '101.236.60.48:8866'},
    {'https': '101.236.21.22:8866'},
    {'https': '222.94.23.50:53281'},
    {'https': '221.228.17.172:8181'},
    {'https': '101.236.18.101:8866'},
    {'https': '118.31.220.3:8080'},
    {'https': '183.48.89.227:8118'},
    {'https': '101.236.60.225:8866'},
    {'https': '106.75.71.122:80'},
    {'https': '27.184.124.252:8118'},
    {'https': '101.236.60.52:8866'},
    {'https': '101.236.19.165:8866'},
    {'https': '106.56.102.185:8070'},
    {'https': '106.56.102.3:8070'},
    {'https': '60.255.186.169:8888'},
    {'https': '106.56.102.213:8070'},
    {'https': '101.236.22.141:8866'},
    {'https': '121.225.26.7:3128'},
    {'https': '36.33.25.209:808'},
    {'https': '106.56.102.98:8070'},
]
# proxy = proxies[random.randint(0,21)]

def getHtml(formdata):
    try:
        response = requests.post(url=start_url, data=formdata, headers=headers, proxies=proxies[random.randint(0, 21)])
        response.close()
        time.sleep(random.randint(1, 4))
        return response
    except TimeoutError as e:
        print(e)

def startHtml():
    #第一页
    token = 1
    response = getHtml(make_form_data(0))
    all_record = eval(response.text)[0]
    s_max = math.floor(all_record / 100)
    # eval将字符串形式转换为等功能的数据形式，获取总条数
    number_list = eval(response.text)[1]
    print(all_record)
    print(s_max)
    getDetail(number_list,token)
    for i in range(1, s_max + 1):
        parse_record_next(i,token)

def getDetail(number_list,token):
    for number in number_list:
        print(number)
        form_data = {
            'action': 'item',
            'p': number[0],
            'croptype': '["粮食作物", "小麦"]',
            '_': ''
        }
        r = getHtml(form_data)
        result = r.json()
        print(result)
        print('第' + str(token) + '条...')
        token += 1
        time.sleep(random.randint(1,4))
        toMongoDB(result)
    print('第一页已爬取完毕...\n 开始爬取下一偏移量的100条数据...')

def getAllCroptype():
    form_data = {
        'action': 'menu',
        '_': ''
    }
    r = getHtml(form_data)
    result = r.text
    print(result)


def make_form_data(fd_num):
    if fd_num == 0:
        # 获取总记录条数的post参数,针对不同页的数据，第一页与其他页的post参数不同，croptype决定查询的种质
        form_data = {
            'action': 'query',
            'p': '{}',
            'croptype': '["粮食作物", "小麦"]',
            '_': ''
        }
    else:
        form_data = {
            'action': 'queryp',
            'p': '{}',
            's': str(fd_num),
            'croptype': '["粮食作物", "小麦"]',
            '_': ''
        }
    return form_data


def parse_record_next(i,token):
    token = token + 1
    response = getHtml(make_form_data(i))
    m = 2
    next_page_number_list = eval(response.text)
    getDetail(next_page_number_list,token)
    m += 1
    print('第'+str(m)+'页已爬取完毕...\n 开始爬取下一偏移量的100条数据...')

def toMongoDB(result):
    client = pymongo.MongoClient(host='localhost',port=27017)
    db = client['cgris']
    cgris = db['first']
    cgris.insert(result)


if __name__ == '__main__':
    startHtml()
