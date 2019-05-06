#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-10-12 17:00
# @Author  : Leo.Liu
# @Site    : 
# @File    : papatest.py
# @Software: PyCharm Community Edition
import urllib
import urllib2

# response = urllib2.urlopen("http://www.baidu.com")

#post
values = {}
values = {"username":"11111@qq.com", "password":"xxxx"}
data = urllib.urlencode(values)
# post
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

# get
geturl = "http://passport.csdn.net/account/login" + "?" + data


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT) '
headers = {"User-Agent": user_agent, 'Referer':'http://www.zhihu.com/articles'}

request = urllib2.Request(url, data, headers)
# request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

# proxy
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# timeout
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
response = urllib2.urlopen('http://www.baidu.com',data, 10)

# put & delete
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)

# debuglog

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')


# URLError
requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(requset)
except urllib2.URLError, e:
    print e.reason

