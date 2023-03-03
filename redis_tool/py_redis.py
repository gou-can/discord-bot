#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/9/10 7:47 下午
    @File: py_redis.py
    @project_name: Yingyue-bot
    # redis 同步操作, 异步操作在tool
"""
import redis

import configger.config


def redis_hget(key, field):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)
    return red.hget(key, field)


def redis_hset(key, field, val):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)
    red.hset(key, field, val)


def redis_hmset(key, mapping):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)
    red.hmset(key, mapping)


def redis_hgetall(key):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)
    return red.hgetall(key)


def redis_sadd(key, val):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)
    red.sadd(key, val)


# 判断val是否存在
def redis_sismember(key, val):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)

    return red.sismember(key, val)


def redis_lpush(key, val):
    red = redis.Redis(host=configger.config.config.cfg['redis']['addr'].split(":")[0], port=6379, db=7)
    red.lpush(key, val)