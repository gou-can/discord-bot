#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/9/26 11:51 上午
    @File: get_key.py
    @project_name: Yingyue-bot
    # 生成redis key的方法
"""


def get_genesis_code_list_key():
    return "discord:producerC:genesis_code:list"


def get_genesis_code_owner_set_key():
    return "discord:producerC:genesis_code:owner:set"


def get_genesis_code_owner_num_key():
    return "discord:producerC:genesis_code:owner:num"
