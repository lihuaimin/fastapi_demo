#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 10:13
# @Author  : Lihuaimin
# @Site    :
# @File    : exception.py 错误统一处理
from enum import Enum

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

from fastapi.exceptions import RequestValidationError
from utils import log

class ExceptionEnum(Enum):
    ALL_ERROR = 10000
    ASSERT_ERROR = 10001
    PARAMETER_ERROR = 10002
    TOKEN_INVALID = 10003
    USER_PASSWORD_ERROR = 10004


# 自定义错误
class UnicornException(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


# token 失效
def token_invalid():
    return UnicornException(ExceptionEnum.TOKEN_INVALID.value, "token失效,请重新登录")


# 用户名密码错误
def user_password_error():
    return UnicornException(
        ExceptionEnum.USER_PASSWORD_ERROR.value, "用户名密码为8-16位字母和数字的组合"
    )


def register_exception(app: FastAPI):
    @app.exception_handler(UnicornException)
    async def unicorn_exception(request: Request, exc: UnicornException):
        log.error("自定义错误" + str(request.url) + exc.message)
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "code": exc.code,
                    "data": None,
                    "msg": exc.message,
                }
            ),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception(request: Request, exc):
        log.error("参数验证错误" + str(request.url) + str(exc))
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "code": ExceptionEnum.PARAMETER_ERROR.value,
                    "data": None,
                    "msg": f"{str(exc)}",
                }
            ),
        )

    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc):
        log.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{exc}")
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "code": ExceptionEnum.ALL_ERROR.value,
                    "data": None,
                    "msg": f"{str(exc)}",
                }
            ),
        )

    @app.exception_handler(AssertionError)
    async def asser_exception_handler(request: Request, exc):
        log.error(f"断言异常\nURL:{request.url}\nHeaders:{request.headers}\n{str(exc)}")
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "code": ExceptionEnum.ASSERT_ERROR.value,
                    "data": None,
                    "msg": f"{str(exc)}",
                }
            ),
        )
