from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(128), index = True)
    title = db.Column(db.String(1024), index = True)
    link = db.Column(db.Text, index = True, unique = True)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title='', pub_date=None, author='', link=''):
        self.title = title
        self.author = author
        if pub_date is None:
            self.pub_date = datetime.utcnow()
        else:
            self.pub_date = pub_date
        self.link = link

    def __repr__(self):
        return '<Article %r>' % self.title

    def to_dict(self):
        return {
            'title': self.title,
            'link': self.title,
            'blog': self.author,
            'published': self.pub_date,
        }

