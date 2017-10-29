from datetime import datetime

import app.spider.rss as rss_tools
from app.models import Article
from app import db

def dict_2_articles():
    url_list = rss_tools.get_all_urls()
    dicts = rss_tools.parser_2_post(url_list)

    art_list = []

    for dic_art in dicts:
        _author = 'Others'
        _title = 'Title'
        _link = 'http://desgard.com'
        _pub_date = datetime.utcnow()

        if 'blog' in dic_art.keys():
            _author = dic_art['blog']
        if 'title' in dic_art.keys():
            _title = dic_art['title']
        if 'link' in dic_art.keys():
            _link = dic_art['link']
        if 'published' in dic_art.keys():
            # TODO:要为每一个博客写 datetime 匹配
            # 先不用这个字段来更新数据,等写出方法后再来补写
            _pub_date = dic_art['published']

        art = Article(title=_title, author=_author, link=_link)
        art_list.append(art)

    return art_list

# API
def cache_update():
    articles = dict_2_articles()

    articles_in_db = Article.query.all()

    for item_db in articles_in_db:
        db.session.delete(item_db)

    db.session.commit()

    for article in articles:
        db.session.add(article)

    db.session.commit()


# API
def cache_query():
    articles_in_db = Article.query.all()
    res_dict = []

    for item_db in articles_in_db:
        res_dict.append(item_db.to_dict())

    return res_dict