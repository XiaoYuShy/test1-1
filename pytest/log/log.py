# -*- coding: utf-8 -*-
# Time : 2023/5/15 21:05
# Author : Xiao Yu
# File : script_3_23.py
# Desc : 日志器，处理器等

import logging
from config.config import log_file

# 创建日志器
logger=logging.getLogger()
# 定义日志器的级别
logger.setLevel(logging.INFO)
# 定义处理器的格式
format=logging.Formatter('%(asctime)s,%(filename)s[line:%(lineno)d]%(levelname) s%(message)s')
# 地址的数据进行了分离，分到了config那边
logFile=log_file
# 创建处理器
fh=logging.FileHandler(logFile,mode='a',encoding='utf-8')
# 设置处理器的级别
fh.setLevel(logging.INFO)
# 设置处理器的格式
fh.setFormatter(format)
# 添加到日志器
logger.addHandler(fh)