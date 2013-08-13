#!/usr/bin/python
from urllib import urlopen
from pyquery import PyQuery as pyq
import httplib, urllib, time
import re

def GetContent():
  url=r'http://verycd.gdajie.com/topics/2960257/'
  url=r'http://www.verycd.com/topics/2960257/'
  content = urllib.urlopen(url).read()
  fp = open('1.html','w')
  fp.write(content)
  fp.close()
  #doc = pyq(content)
  #print doc('li').text()
#GetContent()
#doc = pyq(url=r'http://verycd.gdajie.com/topics/2960257/')
fp = open('1.html', 'r')
content = ''
for line in fp.readlines():
  line = line.strip()
  content += line
fp.close()
doc = pyq(content)
print doc('title').text()
print doc('#catalogGroup').text()
for item in doc('span.title'):
  print doc(item).text()
for item in doc('span.post_origin_img'):
  print doc(item)
  print doc(item).attr('originlink')
