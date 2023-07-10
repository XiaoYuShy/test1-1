# -*- coding: utf-8 -*-
# Time : 2023/5/12 16:50
# Author : Xiao Yu
# File : script_3_23.py
# Desc :

import allure
import pytest

from data import ReadWrite
from objectpage.login_page import Loginpage1
from selenium.webdriver.common.by import By
# 导入日志器
from log.log import logger

#导入web.driver
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#使用sleep功能
from time import sleep
#鼠标移动
from selenium.webdriver.common.action_chains import ActionChains
from config.config import url,driver_path,system_version











class Test_Cases1():

    def test_1(self,login):
        '''
        验证账号密码都合适时的登录
        '''
        self.driver=login
        self.loginpage2=Loginpage1(self.driver)
        print("登录和退出的第一个测试用例")
        self.loginpage2.click_subit()
        sleep(2)
        uesr_list = ReadWrite().excelread('users')
        username = uesr_list[0][0]
        password = uesr_list[0][1]
        self.loginpage2.input_username(username)
        self.loginpage2.input_password(password)
        sleep(3)
        self.loginpage2.click_login()
        # 断言，assertIn:比对信息正不正确，最后是错误的时候返回的信息
        assert '登录 · TesterHome' in self.driver.title
        sleep(3)
        self.loginpage2.xuanzelan()
        sleep(3)
        self.loginpage2.logout()
        # 调用日志器
        logger.info('有效的用户名和密码成功登录系统')

class Test_Cases2():
#
    @pytest.mark.skipif(system_version=='1.1',reason='如果版本号为1.1就执行该装饰器，即不执行该用例')
    def test_2(self,login):
        '''
        验证账号存在时，不输入密码登录，报错后再输入密码进行登录
        '''
        self.driver=login
        self.loginpage2=Loginpage1(self.driver)
        print("登录第二个测试用例")
        sleep(2)
        self.loginpage2.click_subit()
        sleep(2)
        uesr_list=ReadWrite().excelread('users')
        username=uesr_list[0][0]
        password=uesr_list[0][1]
        self.loginpage2.input_username(username)
        self.loginpage2.click_login()
        sleep(2)
        self.loginpage2.input_password(password)
        self.loginpage2.click_login()
        sleep(3)
        self.loginpage2.xuanzelan()
        sleep(3)
        self.loginpage2.logout()
        # 调用日志器
        logger.info('不输入密码先错误，后有效的用户名和密码成功登录系统')

