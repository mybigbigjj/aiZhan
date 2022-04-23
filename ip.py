#批量测试百度权重
#作者：洗澡睡觉

import re
from turtle import pensize
import requests

def get_iplist():
    """获取文件中的url"""
    iplist = []
    with open("url.txt", 'r') as file:   
        data = file.readlines()
        for item in data:
            ip = item.strip()
            iplist.append(ip)            
    return iplist

def dom(w):
    """取出url中的域名"""
    c = w.split(":")
    if len(c) >=3:        
        w = re.findall("http://(.*?):|https://(.*?):",w)[0]
        for i in w:
            if i != "":
                a = i.split(".")
                if len(a) >= 3:
                    if a[-2] == 'com':
                        return a[-3]+"."+a[-2]+"."+a[-1]
                    else:
                        return a[-2]+"."+a[-1]
                else:
                    return i
    else:
        w = re.findall("http://(.+)|https://(.+)",w)[0]
        for i in w:
            if i != "":
                a = i.split(".")
                if len(a) >= 3:
                    if a[-2] == 'com':
                        return a[-3]+"."+a[-2]+"."+a[-1]
                    else:
                        return a[-2]+"."+a[-1]
                else:
                    return i


def aiZan(domain_url):
    """测试百度权重"""
    Private = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  #爱站私钥

    url = 'https://apistore.aizhan.com/baidurank/siteinfos/'+Private+'?domains='+domain_url
    txt =  requests.get(url).text #str 
    baidu = txt.split("\"")
    try:
        if baidu[17] =='msg':
            return print(domain_url +"  -无权重")
    except:
        return print(domain_url +"  -无权重")

    if int(baidu[17]) >= 1 :
        print(" \033[0;31;40m[+]\033[0m "+ domain_url+"的PC权重= "+baidu[17]+" 移动权重= "+baidu[21])
    elif int(baidu[21]) >=1:
        print(" \033[0;31;40m[+]\033[0m " +domain_url+"的PC权重= "+baidu[17]+" 移动权重= "+baidu[21])
    else:
        print(domain_url+"无权重")

if __name__ == "__main__":
    #去从
    url_list = []
    iplist = get_iplist()
    for i in iplist:
        url = dom(i)
        url_list.append(url)

    list2 = list(set(url_list))  #将取出的url写入url_list中并去除重复域名
    for n in list2:
        aiZan(n)
