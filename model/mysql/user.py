#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 14:35
# @Author  : Lihuaimin
# @Site    : 
# @File    : user.py
from connect.mysql import BaseDBModel
from sqlalchemy import Column, String, DATETIME


class DBUser(BaseDBModel):
    __tablename__ = 'user'

    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String)
    user_id = Column(String, primary_key=True)
    register_time = Column(DATETIME)
