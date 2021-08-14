from datetime import datetime
from sql.config import session
from sql.tables import News


def add_Data(list_data):
    for i in list_data:
        print(i['title'][:8]+'...' +"<===>" +"正在写入数据库")
        d = News(
            title = i['title'],
            url = i['url'],
            data = i['data'],
            platform = i['platform'],
            date = datetime.now()
        )
        try:
            session.add(d)
            session.commit()
        except Exception as e:
            session.rollback()

if __name__ == "__main__":
    l = [
        {
        "title":'测试新闻209',
        "url":"http://1.com",
        "platform":'网易',
        "data":'数据',
        }
    ]
    add_Data(l)