# -*- coding: utf-8 -*-
# Time : 2023/5/17 20:31
# Author : Xiao Yu
# File : script_3_23.py
# Desc :公共的fixture函数

# from data import ReadWrite
#
# from objectpage.login_page import Loginpage1
# from selenium.webdriver.common.by import By
# # 导入日志器
# from log.log import logger

#导入web.driver

from selenium.webdriver.edge.service import Service

# #使用sleep功能
# from time import sleep
# #鼠标移动
# from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium import webdriver
from config.config import url,driver_path,system_version




# fixture函数，可以作为参数进行传递,scope='function','class','module','session'
@pytest.fixture(scope='session')   #fixture函数，可以作为参数进行传递
def login():
    print("打开浏览器")
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge(driver_path, options=option)
    # cls.driver = webdriver.Edge('E:\selenium\edgedriver4_win64\msedgedriver.exe',options=option)
    driver.maximize_window()
    driver.get(url)
    yield driver
    print('关闭浏览器')
    driver.quit()



