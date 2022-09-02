#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 17:20
# @Author  : Lihuaimin
# @Site    :
# @File    : __init__.py.py
import uuid
import hashlib
import re


md5 = hashlib.md5()


# 生成UUID
def create_uuid():
    return uuid.uuid1().hex


# md5加密
def enc_md5(enc_str: str):
    md5.update(enc_str.encode("utf-8"))


# 判断是否为纯字母加数字并且8-16位
def is_letter_number(string: str):
    rex = "^[a-zA-Z0-9]{8,16}$"
    return re.findall(rex, string)
