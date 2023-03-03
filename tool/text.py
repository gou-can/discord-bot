#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/23 7:12 下午
    @File: text.py
    @project_name: Yingyue-bot
"""


def get_ids_new(res, _type='str'):
    """
    获得订单的in参数形式(这个时间复杂度小,但是要去列表里要是str类型)
    :return:
    """
    ids = ''
    if isinstance(res, list):
        ids = "','".join(res)
        ids = "'" + ids + "'"

    elif isinstance(res, dict):
        ids = "','".join(res.keys())
        ids = "'" + ids + "'"

    elif isinstance(res, set):
        ids = "','".join(res)
        ids = "'" + ids + "'"
    if _type == 'int':
        ids = ids.replace("'", '')
    return ids
