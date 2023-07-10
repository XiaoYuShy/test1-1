# -*- coding: utf-8 -*-
# Time : 2023/5/17 21:10
# Author : Xiao Yu
# File : script_3_23.py
# Desc :
import subprocess

import pytest



pytest.main()

subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)
subprocess.call('allure open -h 127.0.0.1 - p 8883 ./result/report',shell=True)