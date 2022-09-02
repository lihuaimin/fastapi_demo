#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/31 16:47
# @Author  : Lihuaimin
# @Site    :
# @File    : main.py
import uvicorn

from utils.regist_fastapi import get_app

app = get_app()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8090)
