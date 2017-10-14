import feedparser
import re

feed_url_list = {
    'Guardia': 'http://www.desgard.com/feed.xml',
    'Draveness': 'https://draveness.me/feed.xml',
    'test': 'hehheheh',
}

def get_all_urls():
    res = []
    for title, url in feed_url_list.items():
        res.append(url)
    return res

def parser_2_post(list):
    regex = r"https*://.+feed.xml"
    feed_pattern = re.compile(regex)
    for url in list:
        # 正则检查一下 feed 地址的合法性
        feed_match = feed_pattern.match(url)
        if feed_match == None:
            continue

        # 使用 feedparser 工具来爬取文章信息



if __name__ == '__main__':
    parser_2_post(get_all_urls())

