import pdfkit
import requests
import re
import logging 
import os
from bs4 import BeautifulSoup

"""
url_list

分析解析每一页面的网址构造
构造出列表中的所有教程的网址
用数组保存所有网址并返回数组

"""
def url_list():
    MainURL = 'https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000'
    res = requests.get(MainURL)
    soup = BeautifulSoup(res.content,'html.parser')
    MenuList = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urlset = []
    for li in MenuList.find_all("li"):
        url = 'https://www.liaoxuefeng.com'+ li.a.get('href')
        #print(url)
        urlset.append(url)
    return urlset

"""
解析文章URL,获得Html页面内容
url:需要解析的url
name:保存的html文件名

"""

def parse_url(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'html.parser')
    #获取正文源码
        content = soup.find_all(class_="x-content")[0]
    #print(content)
    #获取文章标题
        title = soup.find('h4').get_text()
        print(title)
    
    #给文章添加标题并加入到文章正文前面,标题处在中间位置
        center_tag = soup.new_tag('center')
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(1,title_tag)
        content.insert(1,center_tag)
    #对文章进行统一编码,解决打开中文乱码
        head = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
        content=head+str(content)
    #print(content)
    #content = str(content)

        content=content.encode('utf-8')
    #content = str(content)
        with open (title+'.html','wb') as f:
            f.write(content)
        return title
    except Exception as e:
        logging.error("parser is failed",exc_info = True) 


def savehtml(urls,file_name):
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
        'custom-header':[('Accept-Encoding','gzip')],
        'cookie':[
            ('cookie-name1','cooik-value1'),
            ('cookie-nmae2','cooik-value2'),
            ],
        
        }
    pdfkit.from_file(urls,file_name,options = options)


def main():
    urls = url_list()
    for i in range(len(urls)):
        parse_url(urls[i])
        


if __name__ == '__main__':
    main()
        
    




