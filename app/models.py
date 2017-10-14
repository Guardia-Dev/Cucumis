from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(128), index = True)
    title = db.Column(db.String(64), index = True)
    link = db.Column(db.String(256), index = True, unique = True)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title = '',pub_date = None, author = '', link = ''):
        self.title = title
        self.author = author
        if pub_date is None:
            self.pub_date = datetime.utcnow()
        else:
            self.pub_date = pub_date
        self.link = link

    def __repr__(self):
        return '<Article %r>' % self.title

    def toDict(self):
        return {
            'title': self.title,
            'url': self.title,
            'author': self.author,
            'public_date': self.pub_date,
        }

