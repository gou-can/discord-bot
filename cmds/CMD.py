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
from business import account_business
from redis_tool import get_key
from redis_tool import tool as redis_ctl


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

        # async def interaction_button():
        #     await self.bot.wait_until_ready()  # 等待bot就绪
        #     await asyncio.sleep(1)
        #     while not self.bot.is_closed():
        #         if self.guild:
        #
        #
        # self.bot.loop.create_task(interaction_button())

    # 错误处理
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        pass

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send("pong")

    # 发送带有按钮的消息
    @commands.command(name='send-message-button-true')
    @commands.check(is_team)
    async def send_msg_button_true(self, ctx):
        item = discord.ui.Button(custom_id='button-ephemeral-true', label='button-ephemeral-true')

        view = discord.ui.View()
        view.add_item(item)
        try:
            await ctx.send("team pong", view=view)
        except Exception as e:
            print(e)

    # 发送带有按钮的消息
    @commands.command(name='send-message-button-false')
    @commands.check(is_team)
    async def send_msg_button_false(self, ctx):
        item = discord.ui.Button(custom_id='button-ephemeral-false', label='button-ephemeral-false')

        view = discord.ui.View()
        view.add_item(item)
        try:
            await ctx.send("team pong", view=view)
        except Exception as e:
            print(e)

    # 斜杠命令 / 消息会引用命了
    # guild_ids 匹配的工会id列表  description 简介 name 指令名称,如果没有就是函数名
    # @commands.slash_command(name='hello-respond', description='hello')
    # async def hello_respond(self, ctx, member: discord.Member, age: int):
    #     # 类似回复指令
    #     await ctx.respond(f"Hello respond, {member}, age{age}!")

    # 斜杠命令,返回不引用命令
    @commands.command(name='hello-send', guild_ids=[996317383935410267], description='hello')
    async def hello_send(self, ctx, member: discord.Member, age: int):
        # 类似回复指令
        await ctx.send(f"Hello respond, {member}, age{age}!")

    # 发送带有按钮的消息

    @commands.command(name='send-genesis-code-message')
    @commands.check(is_team)
    async def send_msg_pk_1122(self, ctx: commands.Context, channel: discord.channel.TextChannel):
        # item = discord.ui.Button(custom_id='pk-message', label='pvp')
        # item2 = discord.ui.Button(custom_id='pk-message-ai', label='pva')
        await account_business.send_genesis_code_msg(ctx, channel)
        await ctx.send("ok")

    @commands.command(name='get-code')
    async def get_code1(self, ctx: commands.Context):
        try:
            num = account_business.init_code(ctx)
        except Exception  as e:
            print(e)
            return
        await ctx.send(f"nu{num}")

    @commands.command()
    @commands.check(is_team)
    async def get_300_member(self, ctx: commands.Context):
        members = ctx.guild.members
        members = [m for m in members if len(m.roles) > 1]
        members.sort(key=lambda x: x.joined_at)
        members = members[:300]
        # print(members)
        owner_key = get_key.get_genesis_code_owner_set_key()
        role = ctx.guild.get_role(1051843859153420388)
        index = 0
        for member in members:
            if await redis_ctl.sismember4set(owner_key, member.id):
                continue
            await member.add_roles(role)
            index += 1
            if index == 290:
                break
        await ctx.send("ok")

    @commands.command(name='send-alpha-role-msg')
    @commands.check(is_team)
    async def send_alpha_role_msg(self, ctx: commands.Context):
        await account_business.send_alpha_role_msg(ctx)

    # @commands.Cog.listener()
    # async def on_interaction(self, interaction):
    #
    #     print("interaction", interaction.custom_id)
    #     # if interaction.custom_id == 'button-ephemeral-true':
    #     #     await interaction.response.send_message("button-ephemeral-true", ephemeral=True)
    #     # elif interaction.custom_id == 'button-ephemeral-false':
    #     #     await interaction.response.send_message("button-ephemeral-false", ephemeral=False)
    #     # else:
    #     #     await interaction.edit_original_message(content='edit')
    #     if 'pk-message-ai' == interaction.custom_id:
    #         await interaction.response.send_message("pk ai", ephemeral=True)
    #     elif 'pk-message' == interaction.custom_id:
    #         if interaction.user.id in cache.Cache.pk_dt:
    #             await interaction.response.send_message("请勿重复参赛", ephemeral=True)
    #             return
    #         pk_user_id = 0
    #         for k, v in cache.Cache.pk_dt.items():
    #             if v == 0:
    #                 pk_user_id = k
    #                 cache.Cache.pk_dt[k] = interaction.user.id
    #                 break
    #         cache.Cache.pk_dt[interaction.user.id] = pk_user_id
    #
    #         await interaction.response.send_message(f"准备挑战", ephemeral=True)
    #
    #         for i in range(30):
    #             print(cache.Cache.pk_dt)
    #             pk_id = cache.Cache.pk_dt.get(interaction.user.id, None)
    #             if pk_id is None:
    #                 return
    #             if pk_id != 0:
    #                 cache.Cache.pk_dt.pop(interaction.user.id)
    #
    #                 await interaction.edit_original_message(
    #                     content=f"匹配成功, {pk_id}v{interaction.user.id}", delete_after=10
    #                 )
    #                 return
    #
    #             index = 30 - i
    #
    #             await interaction.edit_original_message(content=f"匹配剩余时间{index}s", delete_after=10)
    #             i += 1
    #             await asyncio.sleep(1)
    #         cache.Cache.pk_dt.pop(interaction.user.id)
    #         await interaction.edit_original_message(content="pk ai", delete_after=10)




async def setup(bot: commands.Bot):
    await bot.add_cog(CMD(bot))