#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 11:11
# @Author  : Lihuaimin
# @Site    : 
# @File    : middleware.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def register_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )