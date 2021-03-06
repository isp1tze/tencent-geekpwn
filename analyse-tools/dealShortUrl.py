import pandas as pd
import base64
import urllib.parse
import requests
import time
from bs4 import BeautifulSoup
import random
from urllib import request,parse
header_ = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
           "Cookie":"PHPSESSID=uffv7vi2mn7bpr57rlfgup60e2",
           }
temp=[]
urls=[]
urls_=[]
sha1s_=[]
sha1s=[]

def healthyCheck():
    for index in range(len(urls_)):
        if len(str(sha1s_[index]))!=40 or str(urls_[index]) == '""':
            continue
        else:
            sha1s.append(urllib.parse.unquote(str(sha1s_[index])))
            urls.append(urllib.parse.unquote(str(urls_[index])))


def shortString(adj):
    length=int(len(adj)/2)
    result=''
    for i in range(length):
        result=result+adj[i]
    return result

def restore_t_cn(req_url):
    api = 'http://sina.lt/api.php?url=target&action=restore'  #
    try:
        baseUrl = 'http://www.atool.org/shorturl.php'#'http://www.dh.vg/unshort/'
        postData = {
                'url': req_url,
                'd': '2'
        }
        response = requests.post(baseUrl, postData,headers=header_)
        soup = BeautifulSoup(response.content, 'html.parser')
        #url_ = soup.select('.green.strong')
        url_ = soup.select('.green.strong')
        url = str(url_[3]).replace('<td class="green strong"><a href="', '').replace('</a></td>', '').replace(
            '" target="_blank">', '')
        url=shortString(url)
        return url
            # for i in url_:
            #     print(i)
                #url = i['href']
            #print(url)
    except:
        return False

def restore_dwz_cn(url):
    try:
        url = url.replace('www.', '')
        api = 'http://dwz.cn/admin/query'
        postData = {
            'shortUrl': url
        }
        response = (requests.post(api, json=postData))
        url=response.json().get('LongUrl')
        return url
    except:
        return False

def restore_6du_in(url):
    api='https://6du.in/?is_api=1&surl='+url
    response=requests.get(api,)
    response=str(response.content).replace("b'",'').replace("'",'')
    #time.sleep(random.randint(0,5))
    return (response)

def readData(path):
    target=pd.read_csv(path,encoding='UTF-8')
    sha1_temp=target.get('sha1')
    url_temp=target.get('url')
    for sha1 in sha1_temp:
        sha1s_.append(sha1)
    for url in url_temp:
        urls_.append(url)

def detailsDone_t_cn():
    for url in urls_:
        if('http://t.cn' in str(url)):
            temp=restore_t_cn(url)
            if(temp!=False):
                urls.append(temp)
                print(url+"--------->"+temp)
            else:
                urls.append(url)
        else:
            urls.append(url)

def detailsDone_dwz_cn():
    for url in urls_:
        if('dwz' in str(url)):
            temp=restore_dwz_cn(url)
            if(temp!=False and temp!=''):
                urls.append(temp)
                print(url+"--------->"+temp)
            else:
                urls.append(url)
        else:
            urls.append(url)

def detailsDone_6du_in():
    False_=restore_6du_in('www.baidu.com')
    for url in urls_:
        if('http://6du.in' in str(url)):
            temp=restore_6du_in(url)
            temp=temp.replace(' ', '')
            if(temp!=False_ and temp!=''):
                urls.append(temp.replace(' ',''))
                print(url+"--------->"+temp)
            else:
                urls.append(url)
        else:
            urls.append(url)

def main():
    #readData('trace2_test/trojan_web.csv')
    readData("shortRestore(2).csv")
    #detailsDone_dwz_cn()
    #detailsDone_6du_in()
    #detailsDone_t_cn()
    healthyCheck()
    print(len(sha1s))
    print(len(urls))
    dataframe = pd.DataFrame({"sha1": sha1s_,
                              "url": urls})
    dataframe.to_csv("shortRestore(2).csv", index=False, sep=",",encoding='utf_8_sig')


main()