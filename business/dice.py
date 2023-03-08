import asyncio

import discord

dice_lt = ['金', '木', '水', '火', '土']
label_lt = ("✅ 加注Raise", "⛔ 不加Check")
str_not_point = f"""您的武余额不足，请积极参与社群活动获得！！
You don't have enough WU, engage in community activities to earn more!!"""


async def send_steal_msg(ctx, channel):
    print(channel)
    item = discord.ui.Button(custom_id='steal:start', label='开始Start')
    view = discord.ui.View()

    view.add_item(item)
    await channel.send("steal", view=view)