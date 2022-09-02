#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 10:00
# @Author  : Lihuaimin
# @Site    : 
# @File    : __init__.py.py


# from exception import register_exception
from fastapi import FastAPI
from .middleware import register_middleware
from routers import register_routers
from .exception import register_exception
from connect.redis import register_redis


def get_app():
    app = FastAPI()
    register_middleware(app)
    register_exception(app)
    register_routers(app)
    register_redis(app)
    return app
