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
            _pub_date = dic_art['published']

        art = Article(title=_title, author=_author, link=_link)
        art_list.append(art)

    return art_list

def cache_articles():
    articles = dict_2_articles()

    articles_in_db = Article.query.all()

    for item_db in articles_in_db:
        

    for article in articles:
        db.session.add(article)
    db.session.commit()

