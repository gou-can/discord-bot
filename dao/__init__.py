#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/19 11:41 上午
    @File: __init__.py.py
    @project_name: Yingyue-bot
    数据库相关操作
"""

import aiomysql
from configger.config import config as cfg


async def get_mysql_conn(loop):
    config = cfg.cfg
    mysql_config = config["mysql"]

    host = mysql_config['host']
    port = mysql_config['port']
    pwd = mysql_config['password']
    db = mysql_config['database']
    user = mysql_config['user']
    conn = await aiomysql.connect(host=host, port=port, user=user, password=pwd, db=db, loop=loop)
    return conn


async def get_one_4_db(sql, loop):

    conn = await get_mysql_conn(loop)
    try:
        async with conn.cursor() as cur:

            await cur.execute("set time_zone='-7:00';")
            await cur.execute(sql)
            data = await cur.fetchone()
    except Exception as e:
        print("sql<%s>, e:<%s>" % (sql, str(e)))
        conn.close()
        return None
    conn.close()
    return data


async def get_all_4_db(sql, loop):

    conn = await get_mysql_conn(loop)
    try:
        async with conn.cursor() as cur:

            await cur.execute("set time_zone='-7:00';")

            await cur.execute(sql)

            data = await cur.fetchall()
    except Exception as e:
        print(e)
        print("sql<%s>, e:<%s>" % (sql, str(e)))
        conn.close()
        return None

    conn.close()
    return data


async def db_update_or_create(sql, loop):

    conn = await get_mysql_conn(loop)
    try:
        async with conn.cursor() as cur:

            await cur.execute(sql)
            await conn.commit()
    except Exception as e:
        await conn.rollback()
        print(e)
        print("sql<%s>, e:<%s>" % (sql, str(e)))
        conn.close()
        return
    conn.close()
    return True
