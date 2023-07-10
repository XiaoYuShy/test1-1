# -*- coding: utf-8 -*-
# Time : 2023/5/12 21:43
# Author : Xiao Yu
# File : script_3_23.py
# Desc :


from selenium.webdriver.common.by import By

class Loginpage1:
    def __init__(self,driver):
        self.denglu_elem=By.LINK_TEXT,'登录'
        self.user_login_elem=By.ID,'user_login'
        self.user_password_elem=By.ID,'user_password'
        self.commit_elem=By.NAME,'commit'
        self.navbar_elem=By.ID,'navbar-user-menu'
        self.user_logout_elem = By.LINK_TEXT,'退出'
        self.driver=driver



    def click_subit(self):
        self.driver.find_element(*self.denglu_elem).click()


    def input_username(self,username):
        # self.driver.find_element(*self.user_login_elem).clear()
        self.driver.find_element(*self.user_login_elem).send_keys(username)


    def input_password(self, password):
        # self.driver.find_element(*self.user_password_elem).clear()
        self.driver.find_element(*self.user_password_elem).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.commit_elem).click()

    def xuanzelan(self):
        self.driver.find_element(*self.navbar_elem).click()

    def logout(self):
        self.driver.find_element(*self.user_logout_elem).click()


