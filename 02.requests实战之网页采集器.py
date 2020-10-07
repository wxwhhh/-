# -*- codeing = utf-8 -*-
#@Time ：2020/9/18 9:55
#@File :02.requests实战之网页采集器.py

#UA检测：门户网站的服务器会检测对应载体的身份标识为浏览器时，说明请求是一个正常请求
#UA：user-Agent
import requests
if __name__=="__main__":
    #UA伪装：将对应的user-agent封装到一个字典中
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    }
    url = ''#网站网址
    #处理url携带的参数：封装到字典中
    kw = input('输入要搜的关键字:')
    param= {
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求结果中处理了参数
    response = requests.get(url=url,params=param,headers=headers)

    paga_text = response.text
    fileName = kw+".html"
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(paga_text)
    print(fileName,'保存成功！！！！')
