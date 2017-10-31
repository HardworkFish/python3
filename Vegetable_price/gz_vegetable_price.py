#!/usr/bin/csv python
# -*- encoding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib
import  urllib.request
import csv
import codecs
import re
from ast import literal_eval


def CallUrl():
    for page in range (0,2737):
        url = 'http://www.jnmarket.net/import/list-1_'+str(page)+'.html'
        CrawlData(url,page)

def CrawlData(url,page):
    num =  int(page/50)
    response = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(response, 'html.parser')
    tab = soup.find_all('table')[0]
    csvfile = open("gz_vegetables_spider"+str(num)+".csv", 'a+', newline='')
    csvfile.write(str(codecs.BOM_UTF8))
    csvwriter = csv.writer(csvfile)
    tr = tab.find_all('tr')
    for i in range(0,len(tr)):
        data =tr[i].get_text(',',strip=True).split(',')
        for j in range(0,len(data),5):
            csvwriter.writerow([str(i),str(data[j]), str(data[j+1]), str(data[j+2]), str(data[j+3]), str(data[j+4])])
    csvwriter.writerow([" ", " ", " ", " ", " ", " "])


CallUrl()
