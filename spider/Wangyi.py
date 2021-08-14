import requests
import re
import json
from lxml import etree
from pprint import pprint

class wangyi:
    url = " " #find the api of the second newswebsite and type in the url here
    reponses_txt = None

    def __init__(self):
        pass

    def get_basic_data(self):
        self.reponses_txt = requests.get(self.url).text
        return self.reponses_txt[15:-1]

    def ret_basic_data(self):
        primary_data = self.get_basic_data()
        dict_data = re.compile(r'({.*?})',re.S).findall(primary_data)
        for i in dict_data:
            s = json.loads(i)
            yield {
                'title': s['title'],
                'url': s['docurl'],
                'class': "video" if 'v' in s['docurl'] else "article"
            }

    def ret_news_data(self,dataIn:dict):
        dataOut = {
            'title': dataIn['title'],
            'url': dataIn['url'],
            'data': '',
            'platform': '网易新闻'
        }
        # 判断 是 文章 还是视频
        if dataIn['class'] == "article":
            eHtml = etree.HTML(requests.get(dataIn['url']).text)
            pid = (eHtml.xpath('//*[@id="content"]/div[2]/p/@id'))
            data = ''
            for i in pid:
                msg = eHtml.xpath('//*[@id="{i}"]/text()'.format(i=i))
                if msg:
                    data += msg[0]
                else:
                    ftitle = eHtml.xpath('//*[@id="{i}"]/strong/text()'.format(i=i))
                    data += "\n"+ftitle[0]+"\n"
            dataOut['data'] = data
            return dataOut
        else:
            dataOut['data'] = "Video please visit the link"
            return dataOut

    def run(self):
        l = []
        rep_data = self.ret_basic_data()
        for i in rep_data:
            print(i['title']+ "<===>" + "正在爬取")
            msg = self.ret_news_data(i)
            l.append(msg)
        return l



if __name__ == "__main__":
    wy = wangyi()
    pprint(wy.run())