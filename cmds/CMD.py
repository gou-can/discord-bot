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
from business import dice
from business import points


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
        print(error)

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send("pong")

    # 热加载
    @commands.command(name='load-ext', description='热加载, 需要指定加载文件')
    @commands.has_permissions(manage_guild=True)
    async def load_ext(self, ctx, file_name):
        try:
            await self.bot.load_extension(f'cmds.{file_name}')
            await ctx.send(f'load-ext {file_name} ok!')
        except Exception as e:
            await ctx.send(f'load-ext err {str(e)}')

    # 热卸载
    @commands.command(name='unload-ext', description='热卸载,但是不能卸载cmd')
    @commands.has_permissions(manage_guild=True)
    async def unload_ext(self, ctx, file_name: str):
        if file_name.lower() == 'cmd':
            await ctx.send("can't unload cmd")
            return
        try:
            await self.bot.unload_extension(f'cmds.{file_name}')
            await ctx.send(f'unload-ext {file_name} ok!')
        except Exception as e:
            await ctx.send(f'unload-ext err {str(e)}')

    # 热重载
    @commands.command(name='reload-ext', description='热重载, 需要指定重载文件')
    async def reload_ext(self, ctx, file_name):
        try:
            await self.bot.reload_extension(f'cmds.{file_name}')
            await ctx.send(f'reload-ext {file_name} ok!')
        except Exception as e:
            await ctx.send(f'reload-ext err {str(e)}')

    @commands.command(name='points', description='个人积分(测试用,无缓存)')
    async def get_points(self, ctx: commands.Context):
        num = points.get_points(ctx.author.id)
        await ctx.reply(f'{num}')

    @commands.command(name='add-points', description='增加个人积分(测试用,无缓存)')
    async def add_points(self, ctx, num: int):
        points.add_points(ctx.author.id, num)
        await ctx.reply(f'add-points ok')

    @commands.command(name='send-steal-msg')
    async def send_steal_msg1(self, ctx, channel: discord.TextChannel):
        await dice.send_steal_msg(ctx, channel)
        await ctx.send(f'send-steal-msg ok')


async def setup(bot: commands.Bot):
    await bot.add_cog(CMD(bot))