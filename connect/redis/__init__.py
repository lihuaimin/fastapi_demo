#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 17:19
# @Author  : Lihuaimin
# @Site    : 
# @File    : __init__.py.py
from aioredis import create_redis_pool
from config import REDIS_CONNECT
from fastapi import FastAPI


async def get_redis_pool():
    redis = await create_redis_pool(REDIS_CONNECT)
    return redis


def register_redis(app: FastAPI):
    @app.on_event('startup')
    async def startup_event():
        app.state.redis = await get_redis_pool()

    @app.on_event('shutdown')
    async def shutdown_event():
        app.state.redis.close()
        await app.state.redis.wait_closed()
