#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 17:18
# @Author  : Lihuaimin
# @Site    : 
# @File    : __init__.py.py
# 配置项
from urllib.parse import quote_plus as urlquote

userName = 'root'
password = '123456'
dbHost = 'localhost'
dbPort = 3306
dbName = 'fastapi'
MYSQL_CONNECT = f'mysql+pymysql://{userName}:{urlquote(password)}@{dbHost}:{dbPort}/{dbName}?charset=utf8mb4'

REDIS_CONNECT = f'redis://:123456@localhost:6379/0?encoding=utf-8'
