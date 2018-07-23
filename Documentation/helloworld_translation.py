#/usr/bin/env python
#coding=utf8

import http.client
import hashlib
from hashlib import md5
import urllib.request, urllib.parse, urllib.error
import random
import json
import string

#parameters
appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'
q = 'Hello World!'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)
sign = (appid+q+str(salt)+secretKey).encode('utf-8')
m1 = hashlib.md5()
m1.update(sign)
sign = m1.hexdigest()

myurl = '/api/trans/vip/translate'+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
httpClient = None

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    content = str(response.read())
    js_content = json.loads(content[2:-1])
    trans_result = js_content['trans_result']
    print("Original: ", q)
    print("Translation: ", trans_result[-1]['dst'].encode('ascii').decode('unicode-escape'))
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
