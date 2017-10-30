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


urlParse = 'http://sdny.shundeagri.com.cn/price/default.asp?cid=93&page='



def CallPage():

    for pageNum in range (0,130):
        url = urlParse + str(pageNum)
        ParsePage(url,pageNum)


def ParsePage(url,pageNum):


    page = int(pageNum/10)
    csvfile = open('沃尔玛蔬菜平价超市价格' + str(page)+".csv", 'a+', newline='')
    csvfile.write(str(codecs.BOM_UTF8))
    csvwriter = csv.writer(csvfile)
    if(pageNum%10 == 0):
        csvwriter.writerow(["0", "名称", "规格", "价格", "单位", "时间"])
    response = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(response, 'html.parser')
    tab = soup.find_all('table')
    tr = soup.find_all('tr')[15:]
    nameRes = r'<td align="center" bgcolor="#FFFFFF" class="content_list" height="25">(.*?)</td>'
    name = re.findall(nameRes,str(tr),re.S|re.M)
    elseRes = r'<td align="center" bgcolor="#FFFFFF" class="content_list">(.*?)</td>'
    elseData  = re.findall(elseRes,str(tr),re.S|re.M)
    i = 0


    for j in range(0,len(elseData),4):

        csvwriter.writerow([str(i+1),str(name[i]),str(elseData[j]),str(elseData[j+1]),str(elseData[j+2]),str(elseData[j+3])])
        i = i+1

    csvwriter.writerow(["", "", "", "", "", ""])

CallPage()

