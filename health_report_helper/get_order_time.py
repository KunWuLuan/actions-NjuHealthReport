# Copyright 2022 kunwuluan. All Rights Reserved.
# Author-Github: github.com/kunwuluan
# get_order_time.py 2022/4/14 13:01

import requests
from requests import utils,cookies
import json
import ddddocr
import io
import PIL.Image
import re

def convert_Image(img, standard=210):
    image = img.convert('L')
    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] > standard:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    image = image.convert('RGB')
    return image

def verification(img: bytes):
    stream = io.BytesIO(img)
    im = PIL.Image.open(stream)
    im = convert_Image(im)
    buf = io.BytesIO()
    im.save(buf, format='JPEG')
    ocr = ddddocr.DdddOcr(old=True)
    return ocr.classification(buf.getvalue())

login = None
def create_session(username: str, secret: str, nju_edu_cn_cookies: dict[str:str]):
    cur_try, max_try = 0, 10
    while cur_try < max_try:
        s = requests.Session()
        s.get('http://ndyy.nju.edu.cn/NewWeb/')
        verification_resp = s.get('http://ndyy.nju.edu.cn/NewWeb/Ashx/Captcha.ashx?w=80&h=36?')
        res = verification(verification_resp.content)

        global login
        login = s.post('http://ndyy.nju.edu.cn/NewWeb/Ashx/Login.ashx?action=login', params={'params':'{}^{}^{}'.format(username,secret,res)})
        if login.text == '1':
            break
        cur_try = cur_try + 1

    if cur_try == max_try:
        return None
    for k,v in nju_edu_cn_cookies.items():
        cookie = cookies.create_cookie(k, v, domain='.nju.edu.cn')
        s.cookies.set_cookie(cookie)
    return s

def get_order_time(s: requests.Session):
    r = s.get('http://ndyy.nju.edu.cn/NewWeb/Ashx/API_User.ashx?action=selectRWList&page=1&limit=15&params=901')
    j = json.loads(r.content)
    t = []
    for data in j['data']:
        r = s.post('http://ndyy.nju.edu.cn/NewWeb/Ashx/API_User.ashx?action=selectRWYyjlText', params={'params':data['预约任务ID']})
        time = str(r.content, encoding = "utf-8")
        if time != '':
            p = '.*年([0-9]+)月([0-9]+)日'
            t.append('2022-{}-{} 9'.format(*re.match(p, time).groups()))
    return t

def compare_time(default_time: str, order_time: list[str]):
    import time
    import datetime
    from pytz import timezone
    latest_time = time.strptime(default_time,'%Y-%m-%d %H')
    now_time = datetime.datetime.now(timezone('Asia/Shanghai')).timetuple()
    for t in order_time:
        o_t = time.strptime(t,'%Y-%m-%d %H')
        if o_t < now_time and o_t > latest_time:
            latest_time = o_t
    return time.strftime('%Y-%m-%d %-H',latest_time)

def get_time(username, secret, nju_edu_cn_cookies, default_time):
    session = create_session(username, secret, nju_edu_cn_cookies)
    if not session:
        return default_time
    order_time = get_order_time(session)
    return compare_time(default_time, order_time)