# -*- coding: utf-8 -*-
# Time : 2023/5/13 14:35
# Author : Xiao Yu
# File : script_3_23.py
# Desc :

import os

root_path=os.path.dirname(os.path.dirname(__file__))

url='https://testerhome.com/'
driver_path=root_path+r'/driver/msedgedriver.exe'
case_path=root_path+r'/test_demo'
# report_path=root_path+r'/report'
excelpath = root_path+r'/注册登录系统.xlsx'
txtpath = root_path+r'/注册登录系统.txt'
yamlpath = root_path+r'/注册登录系统.yml'
system_version='1.1'
log_file=root_path+r'/log/log.txt'
