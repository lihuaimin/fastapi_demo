#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 17:18
# @Author  : Lihuaimin
# @Site    : 
# @File    : __init__.py.py
from pydantic import BaseModel
from typing import Any


class ResponseModel(BaseModel):
    code: int
    data: Any
    msg: str


def response_200(data: Any):
    return ResponseModel(code=200, data=data, msg='success')


def response_500(msg: str, data=None):
    return ResponseModel(code=500, data=data, msg=msg)