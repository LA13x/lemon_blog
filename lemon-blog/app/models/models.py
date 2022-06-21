# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/17
    File Name: models
    Description:
-------------------------------------------------
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'lemon_users'
    user_id = db.Column(db.BigInteger, primary_key=True)
    user_ip = db.Column(db.String(20), nullable=False)
    user_name = db.Column(db.String(20), index=True, unique=True, nullable=False)
    user_password = db.Column(db.String(15), nullable=False)
    user_email = db.Column(db.String(30), index=True, unique=True, nullable=False)
    user_registration_time = db.Column(db.DATETIME, nullable=False)

    def __str__(self):
        return "<User:{}>".format(self.user_name)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


class Article(db.Model):
    __tablename__ = 'lemon_articles'
    article_id = db.Column(db.BIGINT, autoincrement=True, primary_key=True)
    user_id = db.Column(db.BIGINT, db.ForeignKey('lemon_users.user_id'), nullable=False)
    article_title = db.Column(db.String(255), nullable=False)
    article_content_html = db.Column(db.Text, nullable=False)
    article_content_md = db.Column(db.Text, nullable=False)
    article_comment_count = db.Column(db.BIGINT, nullable=False)
    article_date = db.Column(db.DATETIME)
    article_like_count = db.Column(db.BIGINT, nullable=False)
    article_abstract = db.Column(db.String(255), nullable=True)

    def __str__(self):
        return "<Article title:{}>".format(self.article_title)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result


class Comment(db.Model):
    __tablename__ = 'lemon_comments'
    comment_id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BIGINT, db.ForeignKey('lemon_users.user_id'))
    article_id = db.Column(db.BIGINT, index=True)
    comment_date = db.Column(db.DATETIME, index=True)
    comment_content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return "<Comment content:{}>".format(self.comment_content)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result
