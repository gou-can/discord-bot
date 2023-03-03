#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/9/6 3:51 下午
    @File: tool.py
    @project_name: Yingyue-bot
    # redis 异步操作, 同步操作在py_redis
"""
import aioredis


#  添加数据到集合, 用作去重
import configger.config


async def get_redis_conn(db):
    redis = await aioredis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=db)
    return redis


async def add_val2set(key, val, db=7):
    redis = await get_redis_conn(db)
    await redis.sadd(key, val)
    await redis.close()


async def sismember4set(key, val, db=7):
    redis = await get_redis_conn(db)
    data = await redis.sismember(key, val)
    await redis.close()
    return data


async def redis_get(key, db=7):
    redis = await get_redis_conn(db)
    data = await redis.get(key)
    await redis.close()
    data = data.decode() if data else data
    return data


async def redis_set(key, val, db=7, expire: int = 0):
    redis = await get_redis_conn(db)
    if expire:
        await redis.set(key, val, ex=expire)
    else:
        await redis.set(key, val)
    await redis.close()


async def redis_rpop(key, db=7):
    redis = await get_redis_conn(db)
    data = await redis.rpop(key)
    await redis.close()
    return data.decode() if data else data


async def redis_brpop(key, db=7):
    redis = await get_redis_conn(db)
    data = await redis.brpop(key)
    await redis.close()
    data = data[1]
    return data.decode() if data else data


async def redis_hset(key, field, val, db=7):
    redis = await get_redis_conn(db)

    await redis.hset(key, field, val)
    await redis.close()


async def redis_hget(key, field, db=7):
    redis = await get_redis_conn(db)
    data = await redis.hget(key, field)
    await redis.close()
    return data.decode() if data else data


async def redis_del(key, *keys, db=7):
    redis = await get_redis_conn(db)
    await redis.delete(key, *keys)
    await redis.close()


async def redis_lpush(key, v, db=7):
    redis = await get_redis_conn(db)
    await redis.lpush(key, v)
    await redis.close()


async def redis_lrange(key, start, stop, db=7):
    redis = await get_redis_conn(db)
    data = await redis.lrange(key, start, stop)
    return data


async def redis_incrby(key, val: int, db=7):
    redis = await get_redis_conn(db)
    data = await redis.incrby(key, val)
    await redis.close()
    return data


async def redis_hgetall(key, db=7):
    redis = await get_redis_conn(db)
    data = await redis.hgetall(key)
    return data


async def redis_hincrby(key, field, increment, db=7):
    redis = await get_redis_conn(db)
    await redis.hincrby(key, field, increment)
    await redis.close()