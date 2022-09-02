#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 11:14
# @Author  : Lihuaimin
# @Site    : 
# @File    : user.py
from fastapi import APIRouter, Depends, Request
from dependencies.database import get_db
from model import response_200
from model.schemas.user import UserLogin

router = APIRouter(
    prefix='/user',
    tags=['user'],
    dependencies=[Depends(get_db)]
)


@router.post('/register')
async def register(request: Request, user: UserLogin):
    await request.app.state.redis.set('token1', 123)
    return response_200('success')

