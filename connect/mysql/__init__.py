#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 17:19
# @Author  : Lihuaimin
# @Site    : 
# @File    : __init__.py.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import MYSQL_CONNECT


# 创建数据库引擎
engine = create_engine(MYSQL_CONNECT)
# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 声明基类
BaseDBModel = declarative_base()
