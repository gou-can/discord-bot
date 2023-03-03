#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/16 1:44 下午
    @File: init_config.py
    @project_name: ohdat-discord
"""

import yaml


def init_config(file_name: str):
    with open(file_name, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data

