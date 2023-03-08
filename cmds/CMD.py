#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/17 4:53 下午
    @File: CMD.py
    @project_name: Yingyue-bot
    # 主要方法,操作bot 命令编写
"""

import discord
from discord.ext import commands
from configger.config import config
from cache import Cache
from cmds.classes import CogExtension



# 权限判断装饰器
async def is_team(ctx):
    ok = False
    for role in ctx.author.roles:
        if role.id in config.cfg[Cache.bot_cfg_Key]['MOD_role_ids']:
            ok = True
    return ok


class CMD(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 错误处理
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        pass

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send("pong")


async def setup(bot: commands.Bot):
    await bot.add_cog(CMD(bot))