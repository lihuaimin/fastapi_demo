#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 14:41
# @Author  : Lihuaimin
# @Site    : 
# @File    : user.py
from datetime import time

from pydantic import BaseModel, EmailStr, validator

from utils import is_letter_number

from utils.regist_fastapi.exception import user_password_error

from typing import Union


class UserLogin(BaseModel):
    username: str
    password: str

    @validator('username', 'password')
    def name_must_letter_number(cls, v):
        if not is_letter_number(v):
            raise user_password_error()
        return v


# 注册model
class User(UserLogin):
    email: Union[EmailStr, None] = None
    phone: Union[str, None] = None
    user_id: Union[str, None] = None
    register_time: Union[time, None] = None

    class Config:
        orm_mode = True
