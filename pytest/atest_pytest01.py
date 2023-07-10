# -*- coding: utf-8 -*-
# Time : 2023/5/16 11:06
# Author : Xiao Yu
# File : script_3_23.py
# Desc : pytest框架

import pytest


# fixture函数，可以作为参数进行传递
@pytest.fixture(scope='function',params=[('test001','123456'),('test002','123')])
def login(request):
    # print('打开浏览器')
    # yield
    # print('关闭浏览器')
    return request.param

class TestCases1:

    def test_1(self,login):
        username=login[0]
        password=login[1]
        print(f'第一个测试用例{username},{password}')

    def test_2(self,login):
        username=login[0]
        password=login[1]
        print(f'第二个测试用例{username},{password}')

class TestCases2:

    def test_1(self,login):
        print('第三个测试用例')

    def test_2(self):
        print('第四个测试用例')


if __name__=='__main__':
    pytest.main(['-s','-v'])