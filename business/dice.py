import asyncio
import random

import discord

from business import points
dice_lt = ['金', '木', '水', '火', '土']
label_lt = ("✅ 加注Raise", "⛔ 不加Check")
str_not_point = f"""您的积分余额不足，请积极参与社群活动获得！！
You don't have enough Points, engage in community activities to earn more!!"""
_custom_id = 'steal:start'
_custom_id_raise = 'steal:Raise'
_custom_id_check = 'steal:Check'
_is_update = False
_steal_bet_dt = {}
_steal_choice_dt = {}
_steal_interaction_dt = {}
_once_points = 50


async def send_steal_msg(ctx, channel):
    item = discord.ui.Button(custom_id=_custom_id, label='开始Start')
    item2 = discord.ui.Button( label='开始Start12')
    view = discord.ui.View()

    view.add_item(item)
    view.add_item(item2)
    await channel.send("steal", view=view)


async def listen_steal_start(interaction):
    if interaction.data["custom_id"] != _custom_id:
        return
    if _is_update:
        await interaction.response.send_message(content=
                                                "bot 即将升级维护，该功能暂时不能使用.\n"
                                                "The bot is about to be upgraded for maintenance. "
                                                "This function is temporarily unavailable",
                                                ephemeral=True, )
        return
    user_id = interaction.user.id
    if user_id in _steal_bet_dt:
        await interaction.response.send_message("请勿重复点击!!Do not click repeatedly!!", ephemeral=True,)
        return
    total_point = points.get_points(user_id)

    # 扣除积分
    if total_point >= _once_points:
        points.add_points(user_id, -_once_points)
        _steal_bet_dt[user_id] = _once_points
    else:
        await interaction.response.send_message(str_not_point, ephemeral=True)
        return

    item = discord.ui.Button(custom_id=_custom_id_raise, label=label_lt[0], style=discord.ButtonStyle.green)
    item2 = discord.ui.Button(custom_id=_custom_id_check, label=label_lt[1], style=discord.ButtonStyle.red)
    item3 = discord.ui.Button(custom_id='steal:Betxxxx', label=f"💰投注额Bet [{_once_points}]",
                              disabled=True)

    view = discord.ui.View()
    view.add_item(item)
    view.add_item(item2)
    view.add_item(item3)

    result = [random.choice(dice_lt), random.choice(dice_lt)]

    await interaction.response.send_message(
            content=' '.join(result),
            ephemeral=True,
            view=view,
        )

    print("cache.Cache.steal_bet_dt", _steal_bet_dt)
    for i in range(3):

        # 循环三十次,每秒检查一次是否选择答案
        for _ in range(30):
            await asyncio.sleep(1)
            if _steal_choice_dt.get(user_id):
                _steal_choice_dt[user_id] = None
                break

        if i != 2 and user_id in _steal_interaction_dt:
            try:
                await _steal_interaction_dt[user_id].response.defer()
            except Exception as e:
                print("steal_interaction_dt err", e)
        result.append(random.choice(dice_lt))
        item = discord.ui.Button(custom_id=_custom_id_raise, label=label_lt[0], style=discord.ButtonStyle.green)
        item2 = discord.ui.Button(custom_id=_custom_id_check, label=label_lt[1], style=discord.ButtonStyle.red)
        item3 = discord.ui.Button(custom_id='steal:Betxxxx', label=f"💰投注额Bet [{_steal_bet_dt[user_id]}]", disabled=True)
        view = discord.ui.View()
        view.add_item(item)
        view.add_item(item2)
        view.add_item(item3)
        await interaction.edit_original_response(
            content=' '.join(result),
            view=view
        )
    item = discord.ui.Button(custom_id=_custom_id_raise, label=label_lt[0], style=discord.ButtonStyle.green, disabled=True)
    item2 = discord.ui.Button(custom_id=_custom_id_check, label=label_lt[1], style=discord.ButtonStyle.red, disabled=True)
    item3 = discord.ui.Button(label=f"💰投注额Bet [{_steal_bet_dt[user_id]}]",
                              disabled=True)
    view = discord.ui.View()
    view.add_item(item)
    view.add_item(item2)
    view.add_item(item3)
    await interaction.edit_original_response(
        view=view
    )

    print(f"listen_steal_start<{interaction.user}>", result)
    member = interaction.user.mention
    result_cnt_dt = {}
    max_equal_num = 0
    for i in result:
        c = result.count(i)
        if c > max_equal_num:
            max_equal_num = c
        result_cnt_dt.update({i: c})
    wu = _steal_bet_dt[user_id]
    _steal_bet_dt.pop(user_id)
    # 结算
    if len(result) != 5:
        return
    print("result_cnt_dt", result_cnt_dt)
    if len(result_cnt_dt) == 1:
        if result[0] == dice_lt[0]:  # 黄金清一色
            noun = 8
            t_c = "黄金清一色"
            noun_c = "八倍"
            t_e = 'golden flush'
            noun_e = '8x'

        else:  # 清一色
            noun = 6
            t_c = "清一色"
            noun_c = "六倍"
            t_e = 'flush'
            noun_e = f'{noun}x'
    elif max_equal_num == 4:  # 四条
        noun = 5
        t_c = "四条"
        noun_c = "五倍"
        t_e = 'four of a kind'
        noun_e = f'{noun}x'
    elif max_equal_num == 3 and len(result_cnt_dt) == 2:  # 满堂红
        noun = 4
        t_c = "满堂红"
        noun_c = "四倍"
        t_e = 'full house'
        noun_e = f'{noun}x'
    elif result == dice_lt:
        noun = 3
        t_c = "顺子"
        noun_c = "三倍"
        t_e = 'straight'
        noun_e = f'{noun}x'
    elif max_equal_num == 3:
        noun = 2
        t_c = "三条"
        noun_c = "两倍"
        t_e = 'three of a kind'
        noun_e = f'{noun}x'
    elif max_equal_num == 2 and len(result_cnt_dt) == 3:
        noun = 1
        t_c = "两对"
        noun_c = "一倍"
        t_e = '2 pairs'
        noun_e = f'{noun}x'
    elif max_equal_num == 2:
        noun = 0.5
        t_c = "一对"
        noun_c = "一半"
        t_e = 'a pair'
        noun_e = f'1/2'
    else:
        s = f"""很遗憾{interaction.user.mention}，您此轮无骰型，没有获得积分收益。胜败乃兵家常事，大侠请重新来过！
Sadly {interaction.user.mention} , there isn't a pair in your dice, nor is any Points for your profit. Pull yourself together and come back again."""
        embed = discord.Embed(description=s, color=discord.Color.teal())

        await _steal_interaction_dt[user_id].response.send_message(embed=embed, ephemeral=True)
        if user_id in _steal_interaction_dt:
            del _steal_interaction_dt[user_id]
        return
    money = int(wu * noun)
    base_str = f"""恭喜 {member}，您此轮骰型为`{t_c}`，将获得投注金额的`{noun_c}`，即`{money}`。请再接再厉！
Congrats to {member}, there is `{t_e}` in your dice, you won `{noun_e}` of your bet, which is `{money}`. Come back and play again!!
        """
    embed = discord.Embed(description=base_str, color=discord.Color.teal())

    points.add_points(user_id, money)

    if user_id in _steal_interaction_dt:
        await _steal_interaction_dt[user_id].response.send_message(
            embed=embed,
            ephemeral=True)
        del _steal_interaction_dt[user_id]


async def listen_steal_choice(interaction):
    if interaction.data['custom_id'] not in (_custom_id_raise, _custom_id_check):
        return

    user_id = interaction.user.id

    if _custom_id_raise == interaction.data['custom_id']:

        total_point = points.get_points(user_id)
        if total_point >= _once_points:
            _steal_bet_dt[user_id] += _once_points
            points.add_points(user_id, -_once_points)
        else:
            await interaction.response.send_message(str_not_point, ephemeral=True)
    _steal_interaction_dt[user_id] = interaction
    _steal_choice_dt[user_id] = True
