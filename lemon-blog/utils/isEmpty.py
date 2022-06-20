# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Author: lemon
    Date: 2022/6/19
    File Name: isEmpty
    Description: 判空
-------------------------------------------------
"""


def is_empty(column):
    """
    判断值是否为空
    :param column: 字段字典
    :param msg: 消息字典
    :return:
    """
    for key in column:
        if not column[key]:
            return key

    return False
