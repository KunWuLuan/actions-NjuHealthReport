# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333
# main.py 2021/9/11 13:01
import json
import re
import sys
import logging
import time
import random
import config
import spider
import utils
import secret_update
import get_order_time

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # print(sys.argv[1],end='\n')
        print(re.sub('#(.*)\n', '\n', sys.argv[1]).replace("'", '"'),end='\n')
        config.data = json.loads(re.sub('#(.*)\n', '\n', sys.argv[1]).replace("'", '"'))
        # 以下为本地测试使用
        # print(re.sub(r'\\\'', '\'', sys.argv[1]).replace("'", '"'))
        # config.data = json.loads(re.sub(r'\\\'', '\'', sys.argv[1]).replace("'", '"'))
    if utils.get_GMT8_timestamp() > utils.str_to_timestamp(config.data['deadline'], '%Y-%m-%d'):
        logging.info("超出填报日期")
        exit(-1)
    # retry mechanism
    for _ in range(5):
        try:
            time.sleep(random.randint(0, 10))
            latest_test_time = get_order_time.get_time(config.data['username'], config.data['secret'], config.data['cookies'], config.data['default_time'])

            spider.main(config.data['username'], config.data['password'], config.data['location'], latest_test_time)

            new_secret = {
                'username':config.data['username'],
                'password':config.data['password'],
                'location':config.data['location'],
                'secret':config.data['secret'],
                'cookies':config.data['cookies'],
                'default_time':latest_test_time,
                'git_username':config.data['git_username'],
                'secret_name':config.data['secret_name'],
                'deadline': config.data['deadline'],
                'git_account': config.data['git_account']
            }
            print(json.dumps(new_secret).replace('\"','\\\"'))
            secret_update.update_secret(sys.argv[2], config.data['git_account'], config.data['git_username'], config.data['secret_name'], json.dumps(new_secret).replace('\"','\\\"'))
            break
        except Exception as e:
            if _ == 4:
                raise e
            logging.exception(e)
            time.sleep(5)
