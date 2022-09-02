#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 14:11
# @Author  : Lihuaimin
# @Site    : 
# @File    : database.py
from connect.mysql import SessionLocal
from fastapi.requests import Request


def get_db(request: Request):
    db = SessionLocal()
    try:
        request.state.db = db
        yield db
    finally:
        request.state.db = None
        db.close()
