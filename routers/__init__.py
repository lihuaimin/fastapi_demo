#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 17:21
# @Author  : Lihuaimin
# @Site    : 
# @File    : __init__.py.py
from fastapi import FastAPI
# import user


# 添加api
from routers import user


def register_routers(app: FastAPI):
    app.router.include_router(user.router)
