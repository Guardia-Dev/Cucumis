from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db
from flask_login import UserMixin

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(128), index = True)
    title = db.Column(db.String(64), index = True, unique = True)
    pub_date = db.Column(db.DateTime)
    body = db.Column(db.Text)
    brief = db.Column(db.Text)

    def __init__(self, title = '', body = '', brief = '', pub_date = None, author = ''):
        self.title = title
        self.body = body
        self.author = author
        if pub_date is None:
            self.pub_date = datetime.utcnow()
        else:
            self.pub_date = pub_date
        if brief is '':
            endIndex = min(120, len(self.body))
            self.brief = self.body[:endIndex]
        else:
            self.brief = brief

    def __repr__(self):
        return '<Article %r>' % self.title

    def toDict(self):
        return {
            'title': self.title,
            'author': self.author,
            'public_date': self.pub_date,
            'body': self.body,
        }

