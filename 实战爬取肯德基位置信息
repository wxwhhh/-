# -*- codeing = utf-8 -*-
#@Time ：2020/9/19 17:27
#@File :05.实战爬取肯德基位置信息.py

import requests
if __name__ == "__main__":
    post_url ='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'
    }
    a = int(input('你想爬取的数据页数：'))
    param ={
        'cname': '',
        'pid': '',
        'keyword': '南通',
        'pageIndex': 'a',
        'pageSize': '10',
    }
    response =requests.post(url=post_url,headers=headers,params=param)
    list_data = response.text

    with open('./KFC.html', 'w', encoding='utf-8') as fp:

        fp.write(list_data)

    print('爬取结束!!')
