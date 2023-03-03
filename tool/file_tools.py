#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/30 10:32 上午
    @File: file_tools.py
    @project_name: Yingyue-bot
"""
import io
import os


# 判断文件是否存在
import discord


def file_exist(file_name):
    return os.path.exists(file_name)


def create_path(path):
    try:
        os.mkdir(path)
    except:
        pass


async def send_csv(out_str, channel, file_name):
    data = io.StringIO(out_str)
    file = discord.File(data, f'{file_name}.csv')
    await channel.send(file=file)
    file.close()
    data.close()