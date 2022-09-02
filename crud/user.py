#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 14:47
# @Author  : Lihuaimin
# @Site    : 
# @File    : user.py
from sqlalchemy.orm import Session
from model.mysql.user import DBUser


def get_user_with_userid(db: Session, user_id: str):
    return db.query(DBUser).filter(DBUser.user_id == user_id).first()


def get_all_user(db: Session):
    return db.query(DBUser).all()
