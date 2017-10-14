import feedparser
import re


feed_url_list = {
    'Guardia': 'http://www.desgard.com/feed.xml',
    'Draveness': 'https://draveness.me/feed.xml',
    'Bestswifter': 'https://bestswifter.com/rss/',
    '唐巧': 'http://blog.devtang.com/atom.xml',
    'mikeash': 'https://www.mikeash.com/pyblog/rss.py?mode=fulltext',
    '腾讯科恩实验室官方博客': 'http://keenlab.tencent.com/zh/atom.xml',
    '阿里中间件团队博客': 'http://jm.taobao.org/atom.xml',
}

def get_all_urls():
    res = []
    for title, url in feed_url_list.items():
        res.append(url)
    return res

def parser_2_post(list):
    regex = r"https*://.+"
    feed_pattern = re.compile(regex)
    for url in list:
        # 正则检查一下 feed 地址的合法性
        feed_match = feed_pattern.match(url)
        if feed_match == None:
            continue

        # 使用 feedparser 工具来爬取文章信息
        list_xml = feedparser.parse(url)
        re_serialize(url, list_xml)


def re_serialize(url, rss_json):

    # 博客信息
    # Title 获取自己拟定的字典中取值
    re_feed_url_list = {v:k for k,v in feed_url_list.items()}
    blog_name = re_feed_url_list[url]
    print(blog_name)

    post_list = rss_json['entries']

    # 文章列表
    # 只获取最新的两篇

    cnt = 0
    for post in post_list:
        if cnt is 2:
            break
        cnt += 1

        title = post['title']
        link = post['link']
        published = post['published']
        print(title, link, published)

    print('\n')

if __name__ == '__main__':
    parser_2_post(get_all_urls())

