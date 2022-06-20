# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/20
    File Name: ArticleDetails
    Description:
-------------------------------------------------
"""

import re
from datetime import datetime

from flask import jsonify, request, Response, Blueprint
from app.models.models import User, Article
from flask_sqlalchemy import SQLAlchemy
from utils.isEmpty import is_empty
from utils.getArticles import get_articles_utils

db = SQLAlchemy()
detail = Blueprint('detail', __name__)

msg = {
    'code': '',
    'message': ''
}


@detail.route('/article/<article_id>', methods=['GET'])
def get_article_by_id(article_id):
    """
    获取文章详情页面
    :return:
    """

    if not article_id:
        msg['code'] = '404'
        msg['message'] = '文章id错误'

    article = Article.query.filter(Article.article_id == int(article_id)).first().__dict__

    # 文章数据
    art_data = {
        'id': article['article_id'],
        'title': article['article_title'],
        'html': article['article_content_html'],
        'date': datetime.strftime(article['article_date'], '%Y-%m-%d'),
        'username': User.query.filter(User.user_id == article['user_id']).first().user_name  # 返回作者信息
    }

    data = {
        'code': '200',
        'article': art_data
    }
    return jsonify(data)
