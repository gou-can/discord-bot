#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/17 4:56 下午
    @File: classes.py
    @project_name: Yingyue-bot
"""
from discord.ext import commands

from configger.config import config
from cache import Cache


def get_guild(bot):
    guild = None
    for i in bot.guilds:
        # 服务器id
        if i.id == config.cfg[Cache.bot_cfg_Key]['guild_id']:
            guild = i
            continue
    return guild


class CogExtension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = config.cfg
        self.guild = None
        self.dinosaur_role = None
        self.roles_channel = None
        self.panda_role = None
        self.loop = None
        self.paladin_pioneers_role = None

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.guild:
            # 得到需要定制服务器guild
            self.guild = get_guild(self.bot)

