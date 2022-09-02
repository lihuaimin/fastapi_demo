#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 12:05
# @Author  : Lihuaimin
# @Site    :
# @File    : log.py
from loguru import logger
import os
import datetime

# 项目目录
project_path = os.path.realpath("..")
# 项目日志目录
project_log_dir = os.path.join(project_path, "log")
# 日志文件名
project_log_filename = "runtime_{}.log".format(datetime.date.today())
# 日志文件路径
project_log_path = os.path.join(project_log_dir, project_log_filename)

logger.add(
    # 水槽，分流器，可以用来输入路径
    sink=project_log_path,
    # 日志创建周期
    rotation="00:00",
    # 保存
    retention="1 year",
    # 文件的压缩格式
    compression="zip",
    # 编码格式
    encoding="utf-8",
    # 具有使日志记录调用非阻塞的优点
    enqueue=True,
)


def info(msg: str):
    logger.info(msg)


def debug(msg: str):
    logger.debug(msg)


def success(msg: str):
    logger.success(msg)


def warning(msg: str):
    logger.warning(msg)


def error(msg: str):
    logger.error(msg)


# 崩溃输出
def critical(msg: str):
    logger.critical(msg)
