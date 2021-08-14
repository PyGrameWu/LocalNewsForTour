import time
from spider.Wangyi import wangyi
from spider.Weibo import weibo
from sql.server import add_Data

def run():
    a = wangyi()
    b = weibo()
    while True:
        try:
            wy = a.run()
            add_Data(wy)
        except Exception :
            pass
        try:
            wb = b.run()
            add_Data(wb)
        except Exception:
            pass

        time.sleep(86400) # There are 86400 seconds each day. The spider will mine the data everyday since the code is running. Change the number if you want.

if __name__ == '__main__':
    run()