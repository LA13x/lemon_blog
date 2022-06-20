# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/16
    File Name: lemon_blog
    Description:
-------------------------------------------------
"""

from flask import Flask
from app.api.Users import auth
from app.api.Articles import article
from app.api.ArticleDetails import detail
from flask_cors import CORS
from app.models.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/lemon_blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 注册蓝图
app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(article, url_prefix="/api")
app.register_blueprint(detail, url_prefix="/api")

CORS(app, supports_credentials=True)

db.init_app(app)

if __name__ == '__main__':
    app.run()
