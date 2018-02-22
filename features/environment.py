# -*- coding: utf-8 -*-

from selenium import webdriver

def before_feature(context, feature):
    context.browser = webdriver.Chrome('C:\chromedriver\chromedriver')
    context.browser.set_page_load_timeout(30)