import base64
import pandas as pd
import requests
#http://sina.lt/api.php?url=aHR0cDovL3QuY24vUnFSUVdOdQ==&action=restore
from bs4 import BeautifulSoup
import time
import random
import re
# Base64ed=""
# # temp=''
# #
# # restore_6_in='http://6du.in/?is_api=1&surl='+temp
# #
# # headers = {
# # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
# # 'Cookie':"PHPSESSID=2ke3dsmbd4334kbrsngm6jcg1u; Hm_lvt_fd97a926d52ef868e2d6a33de0a25470=1535447402,1535504679,1535683137; Hm_lpvt_fd97a926d52ef868e2d6a33de0a25470=1535683137; __tins__19242943=%7B%22sid%22%3A%201535683137247%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201535684937247%7D; __51cke__=; __51laig__=1",
# # 'Upgrade-Insecure-Requests':'1',
# # # 'Referer':'https://www.zhihu.com/',
# # # 'X-Requested-With': 'XMLHttpRequest',
# # # 'Origin':'https://www.zhihu.com'
# # }
#
# def t_cn_restore(requests_url):
#     Base64ed=str(base64.urlsafe_b64encode(bytes(requests_url,encoding='gbk')),encoding='gbk')
#     #base64.encode(requests_url,Base64ed)
#     print(Base64ed)
#     restore_t_cn = "http://sina.lt/api.php?url=" + Base64ed + "&action=restore/"
#     print(restore_t_cn)
#     req=requests.session()
#     requests.get(restore_t_cn)
#     response = req.get(restore_t_cn,headers=headers)
#     print(response.json().get('result'))
#     print(response.text)
#     return response#url

def shortString(adj):
    length=int(len(adj)/2)
    result=''
    for i in range(length):
        result=result+adj[i]
    return result

def restore_dwz_cn(url):
    url=url.replace('www.','')
    api='http://dwz.cn/admin/query'
    postData = {
        'shortUrl': url
    }
    response = (requests.post(api, json=postData))
    if(response.json().get('LongUrl')==''):
        print('ddddddddd')
    return (response.json().get('LongUrl'))

def restore(req_url):
    # try:
        baseUrl = 'http://www.atool.org/shorturl.php'#'http://www.dh.vg/unshort/'
        postData = {
            'url': req_url,
            'd': '2'
        }
        response = requests.post(baseUrl, postData)
        soup = BeautifulSoup(response.content, 'html.parser')
        url_ = soup.select('.green.strong')
        url=str(url_[3]).replace('<td class="green strong"><a href="','').replace('</a></td>','').replace('" target="_blank">','')
        url=shortString(url)
        print(url)
        #print(re.match("^.+h",url))
        # for i in url_:
        #     print(i)
            #url = i['href']
        #print(url)
    # except:
    #     print('Error!')
    #     return False
        return url
def restore_6du_in(url):
    api='http://6du.in/?is_api=1&surl='+url
    response=requests.get(api)
    print(str(response.content))
def main():
    # target = pd.read_csv('trojan_web.csv', encoding='utf_8_sig')
    # sha1=target.get('sha1')
    # urls = target.get('url')
    # change=[]
    # sha1_key=[]
    # for sha1_ in sha1:
    #     sha1_key.append(sha1_)
    # for url in urls:
    #     temp=restore(url)
    #     if temp!=False:
    #         url=temp
    #     change.append(url)
    #     time.sleep(random.uniform(0.5,1))
    # dataframe = pd.DataFrame({"sha1": sha1_key,
    #                           "url": change})
    #
    # dataframe.to_csv("shortRestore.csv", index=False, sep=",")
    test_='http://6du.in/791cxB'#''
    restore_dwz_cn('www.baidu.com')#('http://dwz.cn/de3rp2Fl')#('http://dwz.cn/3WLZ54')
main()
#print(urls)