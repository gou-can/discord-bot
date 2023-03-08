#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/19 2:13 下午
    @File: configger.py
    @project_name: Yingyue-bot
"""
import yaml


class Config:
    def __init__(self, file_name='./config.yaml'):
        self.cfg = init_config(file_name)


def init_config(file_name):
    with open(file_name, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data


config = Config()
