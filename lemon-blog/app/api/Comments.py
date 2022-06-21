# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/20
    File Name: Comments
    Description:
-------------------------------------------------
"""
import re
from datetime import datetime

from flask import jsonify, request, Blueprint
from app.models.models import User, Comment, Article
from flask_sqlalchemy import SQLAlchemy
from utils.isEmpty import is_empty
from app.models.models import db

# db = SQLAlchemy()
comment = Blueprint('comment', __name__)

msg = {
    'code': '',
    'message': ''
}


@comment.route('/comment', methods=['POST'])
def post_comment():
    """
    评论提交
    :return:
    """
    data = request.get_json()
    if not data:
        msg['code'] = '404'
        msg['message'] = 'not json!'
        return jsonify(msg)

    article_id = data.get('article_id', None)
    comment_date = datetime.now()
    user_name = data.get('user', None)
    comment_content = data.get('comment', None)

    user_id = User.query.filter(User.user_name == user_name).first().user_id
    resultArt = Article.query.filter(Article.article_id == article_id).first()
    resultArt.article_comment_count  += 1

    test = {
        'article_id': article_id,
        'comment_content': comment_content,
        'user_id': user_id,
        'comment_date': comment_date,
    }
    # 校验字段是否为空
    result = is_empty(test)
    if result:
        msg['code'] = '404'
        msg['message'] = result + '不能为空！'
        return jsonify(msg)

    commentPost = Comment()

    commentPost.comment_date = comment_date
    commentPost.user_id = user_id
    commentPost.article_id = article_id
    commentPost.comment_content = comment_content

    db.session.add(commentPost)
    db.session.commit()

    db.session.add(resultArt)
    db.session.commit()

    db.session.close()

    msg['code'] = '200'
    msg['message'] = '评论发表成功'
    return jsonify(msg)


@comment.route('/comment/<article_id>', methods=['GET'])
def get_comments(article_id):
    """
    获取某篇文章的所有评论
    @:param article_id: 文章id
    :return:
    """
    comments = Comment.query.filter(Comment.article_id == article_id).all()
    comment_list = []
    for i in comments:
        comment_list.append(i.__dict__)

    comment_data = {}
    for i in range(len(comment_list)):
        comment_data['comment_' + str(i)] = {
            'comment_id': comment_list[i]['comment_id'],
            'comment_content': comment_list[i]['comment_content'],
            'comment_user': User.query.filter(User.user_id == comment_list[i]['user_id']).first().user_name,
            'comment_date': datetime.strftime(comment_list[i]['comment_date'], '%Y-%m-%d')
        }

    data = {
        'code': '200',
        'comments': comment_data
    }
    return jsonify(data)
