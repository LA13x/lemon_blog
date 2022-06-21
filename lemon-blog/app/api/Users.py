# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/17
    File Name: Users
    Description: 用户登录注册相关api
-------------------------------------------------
"""
import datetime
import re

from flask import jsonify, request, Response, Blueprint
from app.models.models import User, Article
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_

db = SQLAlchemy()
auth = Blueprint('auth', __name__)

msg = {
    'code': '',
    'message': ''
}


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        msg['code'] = '404'
        msg['message'] = 'not json!'
        return jsonify(msg)

    username = data.get('username', None)
    password = data.get('password', None)
    email = data.get('email', None)

    if 'username' not in data or not username:
        msg['code'] = '404'
        msg['message'] = '请提供一个合法用户名！'
        return jsonify(msg)

    if 'password' not in data or not password:
        msg['code'] = '404'
        msg['message'] = '请提供一个有效的密码！'
        return jsonify(msg)

    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, email):
        msg['code'] = '404'
        msg['message'] = '请提供一个有效的邮箱地址！'
        return jsonify(msg)

    if User.query.filter(or_(User.user_name == username, User.user_email == email)).first():
        msg['code'] = '404'
        msg['message'] = '用户名或邮箱已存在！'
        return jsonify(msg)

    ip = request.remote_addr
    user = User()
    user.user_name = username
    user.user_ip = ip
    user.user_registration_time = datetime.datetime.now()
    user.user_password = password
    user.user_email = email

    db.session.add(user)
    db.session.commit()

    msg['code'] = '200'
    msg['message'] = '注册成功'

    return jsonify(msg)


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username', None)
    password = data.get('password', None)

    if 'username' not in data or not username:
        msg['code'] = '404'
        msg['message'] = '请提供一个合法用户名！'
        return jsonify(msg)

    if 'password' not in data or not password:
        msg['code'] = '404'
        msg['message'] = '请提供一个有效的密码！'
        return jsonify(msg)

    if not User.query.filter(and_(User.user_name == username, User.user_password == password)):
        msg['code'] = '404'
        msg['message'] = '用户名或密码错误！'
        return jsonify(msg)

    msg['code'] = '200'
    msg['message'] = '登录成功'
    msg['user'] = username

    return jsonify(msg)
