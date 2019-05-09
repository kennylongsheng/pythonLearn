#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_opt.add_experimental_option("prefs", prefs)


def login():
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://i.weidian.com/")
    time.sleep(3)
    browser.find_element_by_link_text("登录/注册").click()
    time.sleep(3)
    browser.find_element_by_id("login_init_by_login").click()
    time.sleep(2)
    username = browser.find_element_by_id("login_isRegiTele_input")
    password = browser.find_element_by_id("login_pwd_input")
    username.send_keys("###")
    password.send_keys("###")
    browser.find_element_by_link_text("登录").click()
    time.sleep(3)
    browser.get("https://weidian.com/cart/")
    time.sleep(3)

def refresh1():
    browser.refresh()
    while True:
        try:
            browser.find_element_by_id("submit_order").click()
            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print(f"OrderTime:{now1}")
        except:
            browser.refresh()

def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if(now >= times):
            browser.find_element_by_xpath("//span[.='去结算(1)']").click()
            try:
                browser.find_element_by_id("submit_order").click()
                now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                print(f"OrderTime:{now1}")
                print("End")
            finally:
                break
                refresh1()
        print(now)

if __name__ == "__main__":
    times = "2019-01-07 20:57:30.000000"
    browser = webdriver.Chrome(chrome_options=chrome_opt)
    login()
    buy(times)
