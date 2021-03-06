# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/19
    File Name: Articles
    Description:
-------------------------------------------------
"""

import re
from datetime import datetime

from flask import jsonify, request, Response, Blueprint
from app.models.models import User, Article, Comment
from utils.isEmpty import is_empty
from app.models.models import db
from utils.getArticles import get_articles_utils

article = Blueprint('article', __name__)

msg = {
    'code': '',
    'message': ''
}


@article.route('/post/article', methods=['POST'])
def post_article():
    """
    文章提交
    :return:
    """
    data = request.get_json()
    if not data:
        msg['code'] = '404'
        msg['message'] = 'not json!'
        return jsonify(msg)

    articlePost = Article()

    article_id = data.get('id', None)
    article_title = data.get('articleTitle', None)
    article_content_md = data.get('articleContentMd', None)
    article_content_html = data.get('articleContentHtml', None)
    article_content_abstract = data.get('articleAbstract', None)
    article_date = datetime.now()
    user_name = data.get('username', None)

    user_id = User.query.filter(User.user_name == user_name).first().user_id

    test = {
        'article_title': article_title,
        'article_content_md': article_content_md,
        'article_content_html': article_content_html,
        'article_content_date': article_date,
        'user_id': user_id
    }
    # 校验字段是否为空
    result = is_empty(test)
    if result:
        msg['code'] = '404'
        msg['message'] = result + '不能为空！'
        return jsonify(msg)

    articlePost.article_id = article_id
    articlePost.article_title = article_title
    articlePost.article_date = article_date
    articlePost.article_content_md = article_content_md
    articlePost.article_content_html = article_content_html
    articlePost.user_id = user_id
    articlePost.article_abstract = article_content_abstract
    articlePost.article_like_count = 0
    articlePost.article_comment_count = 0

    db.session.add(articlePost)
    db.session.commit()
    db.session.close()

    msg['code'] = '200'
    msg['message'] = '发表成功'
    return jsonify(msg)


@article.route('/get/articles', methods=['GET'])
def get_article_numbers():
    """
    获取所有文章数量
    :return:
    """
    article_numbers = Article.query.count()

    data = {
        'code': '200',
        'article_numbers': article_numbers
    }
    return jsonify(data)


@article.route('/get/articles/<page>', methods=['GET'])
def get_articles(page):
    """
    获取指定页面的文章
    @:param page: 请求页面号
    :return:
    """
    articles = Article.query.order_by(Article.article_date.desc()).all()
    article_list = []
    for i in articles:
        article_list.append(i.__dict__)

    # 一页六个文章
    index = (int(page) - 1) * 6
    article_list = article_list[index:index + 6]

    art_data = {}
    for i in range(len(article_list)):
        art_data['article_' + str(i)] = {
            'id': article_list[i]['article_id'],
            'title': article_list[i]['article_title'],
            'abstract': article_list[i]['article_abstract'],
            'date': datetime.strftime(article_list[i]['article_date'], '%Y-%m-%d'),
            'username': User.query.filter(User.user_id == article_list[i]['user_id']).first().user_name  # 返回作者信息
        }
        # print(User.query.filter(Article.user_id == article_list[i]['user_id']).first().user_id)
    data = {
        'code': '200',
        'articles': art_data
    }
    return jsonify(data)


@article.route('/get/<user>/articles', methods=['GET'])
def get_user_articles(user):
    """
    获取特定用户的所有文章
    :return:
    """
    user_id = User.query.filter(User.user_name == user).first().user_id
    articles = Article.query.order_by(Article.article_date.desc()).filter(Article.user_id == user_id).all()
    article_list = []
    for i in articles:
        article_list.append(i.__dict__)

    art_data = get_articles_utils(article_list)

    data = {
        'code': '200',
        'articles': art_data
    }
    return jsonify(data)


@article.route('/get/<user>/articles/<page>', methods=['GET'])
def get_user_articles_page(user, page):
    """
    获取特定用户的指定页文章
    :param user: 用户身份
    :param page: 页码号
    :return:
    """
    user_id = User.query.filter(User.user_name == user).first().user_id
    articles = Article.query.order_by(Article.article_date.desc()).filter(Article.user_id == user_id).all()
    article_list = []
    for i in articles:
        article_list.append(i.__dict__)

    index = (int(page) - 1) * 4
    article_list = article_list[index:index + 4]

    art_data = get_articles_utils(article_list)

    data = {
        'code': '200',
        'articles': art_data
    }
    return jsonify(data)


@article.route('/update/article', methods=['POST'])
def update_article():
    """
    文章提交
    :return:
    """
    data = request.get_json()
    if not data:
        msg['code'] = '404'
        msg['message'] = 'not json!'
        return jsonify(msg)

    article_id = data.get('id', None)
    article_title = data.get('articleTitle', None)
    article_content_md = data.get('articleContentMd', None)
    article_content_html = data.get('articleContentHtml', None)
    article_content_abstract = data.get('articleAbstract', None)
    # user_name = data.get('username', None)
    #
    # user_id = User.query.filter(User.user_name == user_name).first().user_id

    test = {
        'article_title': article_title,
        'article_content_md': article_content_md,
        'article_content_html': article_content_html,
    }
    # 校验字段是否为空
    result = is_empty(test)
    if result:
        msg['code'] = '404'
        msg['message'] = result + '不能为空！'
        return jsonify(msg)

    # 查询出目标文章并进行修改

    target_article = Article.query.filter(Article.article_id == article_id).first()

    target_article.article_content_md = article_content_md
    target_article.article_content_html = article_content_html
    target_article.article_title = article_title
    target_article.article_abstract = article_content_abstract

    db.session.add(target_article)
    db.session.commit()
    db.session.close()

    msg['code'] = '200'
    msg['message'] = '修改成功'
    return jsonify(msg)


@article.route('/delete/article/<article_id>', methods=['GET'])
def delete_article(article_id):
    """
    删除指定文章
    :param article_id: 文章id
    :return:
    """

    # 删除思路：找出对应的文章id，删除此条记录，然后找到评论表中对应的文章id，删除对应的此文章的所有评论
    data_item = Article.query.filter(Article.article_id == article_id).first()

    if not id:
        msg['code'] = '404'
        msg['message'] = '请传入有效文章id'

    db.session.delete(data_item)
    db.session.commit()

    comments = Comment.query.filter(Comment.article_id == article_id).all()
    for i in comments:
        db.session.delete(i)
        db.session.commit()

    db.session.close()
    msg['code'] = '200'
    msg['message'] = '删除文章成功'

    return jsonify(msg)
