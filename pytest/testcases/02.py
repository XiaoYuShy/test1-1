# -*- coding: utf-8 -*-
# Time : 2023/5/16 11:06
# Author : Xiao Yu
# File : script_3_23.py
# Desc : pytest框架
import allure
import pytest


# fixture函数，可以作为参数进行传递,scope='function','class','module','session'
# @pytest.fixture(scope='function')
# # def login():
# #     print('打开浏览器')
# #     yield
# #     print('关闭浏览器')

@allure.feature('登录模块2')
class aTestCases3:

    @pytest.mark.run(order=2)
    @pytest.mark.skipif(2<3,reason='强制跳过')
    def test_1(self,login):
        print('第五测试用例')

    @allure.story('登录成功的测试用例')
    @pytest.mark.parametrize('username,password',[('tester001','12345'),('tester002','123456')])
    def test_2(self,username,password):
        with allure.step('输入用户名和密码'):
            print(f'用户名和密码：{username},{password}')
        with allure.step('点击登录'):
            print('登录！！！')

@allure.feature('登录模块1')
class aTest_Cases4:

    @allure.story('登录失败的测试用例')
    @pytest.mark.run(order=1)
    def test_3(self,login):
        with allure.step('啥也没输入'):
            print('登录失败')


if __name__=='__main__':
    pytest.main(['-s','-v'])