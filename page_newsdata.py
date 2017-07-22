import urllib.request
import re
import requests
from bs4 import BeautifulSoup
url="http://npaac.scau.edu.cn/a/gonggao/"
headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Refer' : url
        
        }
res={}
res = requests.get(url) 
res.encoding = 'UTF-8'

soup = BeautifulSoup(res.text, 'html.parser')
num=soup.select(".pagelist li")[0].text
num1=re.findall(r"\d+\.?\d*",num)[1]
num2=int(num1)
print(num2)
def saveHtml(file_name,file_content):
    #with open (file_name.replace('/','_')+".html","a+",encoding='UTF-8') as f:
    with open (file_name+".html","a+",encoding='UTF-8') as f:

        f.write( file_content)
       
def Content(url_data):
    
    #url_data="http://npaac.scau.edu.cn/a/gonggao/2017/0621/413.html"
    res=requests.get(url_data)
    res.encoding='UTF-8'
    content=res.text
    soup=BeautifulSoup(res.text,'html.parser')
    tables=soup.select('.productDesc')
    print(tables)
    return tables

for new in range(3,num2+3):
    link=soup.select('.w1002 a')[new]['href']
    truelink="http://npaac.scau.edu.cn"+link
    head='<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'

    content=Content(truelink)
    saveHtml(str(new-2),str(head))
    saveHtml(str(new-2),str(content))
    print("=====================================================")



   
