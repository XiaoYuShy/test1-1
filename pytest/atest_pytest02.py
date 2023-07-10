# -*- coding: utf-8 -*-
# Time : 2023/5/16 11:06
# Author : Xiao Yu
# File : script_3_23.py
# Desc : pytest框架

import pytest


# fixture函数，可以作为参数进行传递,scope='function','class','module','session'
@pytest.fixture(scope='function')
def login():
    print('打开浏览器')
    yield
    print('关闭浏览器')


class TestCases3:

    @pytest.mark.run(order=2)
    @pytest.mark.skipif(2<3,reason='强制跳过')
    def test_1(self,login):
        print('第五测试用例')
    @pytest.mark.parametrize('username,password',[('tester001','12345'),('tester002','123456')])
    def test_2(self,username,password):
        print(f'第六测试用例{username},{password}')

class Test_Cases4:
    # @pytest.mark.flaky(reruns=5)
    @pytest.mark.run(order=1)
    def test_3(self,login):
        # assert 2>3
        print('第七测试用例')


if __name__=='__main__':
    pytest.main(['-s','-v'])