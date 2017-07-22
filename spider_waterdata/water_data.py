import urllib.request
import re
import requests
import pdfkit

from bs4 import BeautifulSoup
#"http://pub.gdepb.gov.cn/pub/pubcatalogwry/extranet_pub_documents_list.jsp"
#"http://pub.gdepb.gov.cn/pub/pubcatalogwry/extranet_pub_document_view.jsp?docId=77000"
SourceURL="http://www.gdep.gov.cn/zdgk/sz/201707/t20170706_225419.html"
headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Refer' : SourceURL
        
        }
#获得水环境数据页面源码函数
def WaterData(url):
    res={}
    res = requests.get(url)
    data=urllib.request.urlopen(url).read()
    data=data.decode('GBK')
    soup = BeautifulSoup(data, 'html.parser')
    data1= soup.select('.holder ')
   # data1="<head><meta http-equiv='Content-Type' content='text/html; charset='utf-8'/></head>"+data1
    print(data1)
    return data1
#构造出各个页面的链接函数
def GetLink(TrueLink):
    frontLink='http://www.gdep.gov.cn'
    res=requests.get(TrueLink)
    res.encoding='UTF-8'
    content=res.text
    soup=BeautifulSoup(res.text,'html.parser')
    
    link=frontLink+soup.select('.listimg_data a ')[0]['href'][2:]
    return link
'''MyURL='http://www.gdep.gov.cn/swrfz/'
content=GetLink(MyURL)
print(content)'''
def GetTotalPages(TrueLink):
    res=requests.get(TrueLink)
    res.encoding='GBK'
    content=res.text
    soup=BeautifulSoup(res.text,'html.parser')
    Pagesnumber=soup.select('.page-box tr')[0].text
    MyURL='http://www.gdep.gov.cn/swrfz/'
    number=GetTotalPages(MyURL)
    print(number)
    return Pagesnumber
def saveHtml(file_name,file_content):
    #with open (file_name.replace('/','_')+".html","a+",encoding='UTF-8') as f:
    with open (file_name+".html","a+",encoding='UTF-8') as f:
        f.write( file_content)
    pdfkit.from_file(file_name+".html",'out.pdf')
def URLtoPDF(MyURL):
   # MyURL='http://www.gdep.gov.cn/swrfz/'
   
    content=GetLink(MyURL)
    #String=WaterData(content)
   # print(String)
    pdfkit.from_url(content,'out.pdf')
    
    print(content)


MyURL='http://www.gdep.gov.cn/swrfz/'
link=GetLink(MyURL)
print(link)
#URLtoPDF(MyURL)
head='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
saveHtml('myout',head)
saveHtml('myout',str(WaterData(link)))
    
    
    
