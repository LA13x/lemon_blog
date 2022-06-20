# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/20
    File Name: getArticles
    Description:
-------------------------------------------------
"""
from datetime import datetime


def get_articles_utils(article_list):
    art_data = {}
    for i in range(len(article_list)):
        art_data['article_' + str(i)] = {
            'id': article_list[i]['article_id'],
            'title': article_list[i]['article_title'],
            'abstract': article_list[i]['article_abstract'],
            'date': datetime.strftime(article_list[i]['article_date'], '%Y-%m-%d'),
        }
    return art_data
