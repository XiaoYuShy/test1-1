# -*- coding: utf-8 -*-
# Time : 2023/5/12 19:09
# Author : Xiao Yu
# File : script_3_23.py
# Desc :


import unittest
from BeautifulReport import BeautifulReport
from config.config import case_path,report_path

#加载批量的测试用例，要先设置根节点
suite=unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')
# txt文本生成
# runner=unittest.TextTestRunner()
# runner.run(suite)
result=BeautifulReport(suite)
#第一个用例名称，第二个测试报告的名字,第三个测试报告的地址
result.report(description='系统登录的测试报告',filename='SIT测试报告',report_dir=report_path)