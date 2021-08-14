import requests
import re


class weibo:
    k = [
        r'''['|"]http.*?["|']''',
        r'''href.*?["|']surl-text["|']>''',
        r'<a',
        r'</a>',
        r'<br />',
        r'<span.*?/>',
        r'</span>',
        r'data-url=',
        r'... href=.*?>全文',
        r'href= data-hide="">',
        r'网页链接'
    ]
    url = '' #find the api of the first newswebsite and type in the url here
    def ret_news_data(self):
        try:
            responses = requests.get(self.url).json()
            for i in range(len(responses['data']['cards'])):

                try:
                    comm = responses['data']['cards'][i]['mblog']['text']
                    name = responses['data']['cards'][i]['mblog']['user']['screen_name']
                    url = responses['data']['cards'][i]['scheme']
                    # 清洗 数据
                    for s in self.k:
                        comm = (re.sub(s, '', comm, re.S))

                    yield {
                        'title': name,
                        'url': url,
                        'data': comm.replace(' ',''),
                        'platform': 'weibo hot keywords'
                    }
                except Exception as e:
                    pass
        except Exception as e:
            pass

    def run(self):
        l = []
        for i in self.ret_news_data():
            l.append(i)
        return l


if __name__ == "__main__":
    a = weibo()
    b = a.ret_news_data()
    for i in b:
        print(i)