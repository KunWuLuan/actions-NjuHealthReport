# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333
# config.py 2021/9/11 13:01

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s\t%(levelname)s\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename='../../../log/log.txt'
)

# The data you need to fill
data = {
    # fill them:
    'username': 'fill-it',  # 学号
    'password': 'fill-it',  # 密码
    'location': 'fill-it',  # 地址, 如 中国xx省xx市xx区xxxx
    'deadline': '2021-10-05', # 填报截止日期，超过该天则停止填报并报错到 actions，开区间

    'none': 'none'
}


# Don't edit this variables above
HEADERS = {
    "Host":"ehallapp.nju.edu.cn",
    "Connection":"keep-alive",
    "Accept":"application/json, text/plain, */*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; k30pro Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36  cpdaily/8.2.15 wisedu/8.2.15",
    "Referer":"http://ehallapp.nju.edu.cn/xgfw/sys/mrjkdkappnju/index.html",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,en-US;q=0.8",
    "X-Requested-With":"com.wisedu.cpdaily.nju",
}
HEADERS1 = {
    "Host":"ndyy.nju.edu.cn",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "cookie": "pgv_pvi=3544430592; _ga=GA1.3.1811201301.1571291980; zg_did=%7B%22did%22%3A%20%221770fa3bcd5162-025f0c21f6f9cd-326e7006-1aeaa0-1770fa3bcd6d07%22%7D; zg_=%7B%22sid%22%3A%201633936399837%2C%22updated%22%3A%201633936407394%2C%22info%22%3A%201633936399840%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22MG1933068%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201633936399837%7D; ASP.NET_SessionId=5bcwsyyrv2st1rfye2ym3jcg; iPlanetDirectoryPro=VVpls0lRTalbW7reXvy6gk",
    "Referer": "http://ndyy.nju.edu.cn/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}
