#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/16 1:38 下午
    @File: main.py
    @project_name: ohdat-discord
"""
import asyncio
import os

import cache
import init_config
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

if __name__ == '__main__':
    print("discord.py version:", discord.__version__)

    config = init_config.init_config('./config.yaml')
    loops = asyncio.get_event_loop()
    task_lt = []

    # 加载cmds下的方法
    for file_name in os.listdir('./cmds'):
        if file_name != '__init__.py' and file_name != 'classes.py' and file_name.endswith('.py'):
            task_lt.append(bot.load_extension(f'cmds.{file_name[:-3]}'))
            # await bot.load_extension(f'cmds.{file_name[:-3]}')
    loops.run_until_complete(asyncio.wait(task_lt))
    bot.run(config[cache.Cache.bot_cfg_Key]['token'])

