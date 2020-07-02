# -*- coding:utf-8 -*-

import os, time, unittest
import yaml

from selenium import webdriver
from appium import webdriver
from app.getApk import *


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

cur_path = os.path.abspath(os.path.dirname(__file__))
caps_path = os.path.join(os.path.join(cur_path,'locate'),'CreatGroup.yml')
print(cur_path)

def read_caps():
    with open(caps_path,'r',encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data
#ci_apk()
#replace_package()

desired_caps = {}

desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '7.1.1'  # 设备系统版本
desired_caps['deviceName'] = '9a57fa4a'  # 设备名称
desired_caps['automationName'] = 'uiautomator2'
desired_caps['appPackage'] = 'com.xueqiu.android'
#desired_caps['unicodeKeyboard'] = True
#desired_caps['resetKeyboard']=True
desired_caps['noReset']=True
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
desired_caps['app'] ="/Users/xueqiu/PycharmProjects/AppiumPython/app/xueqiu.apk"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

driver.implicitly_wait(10)

time.sleep(5)
"""
click_hangqing_loc=("id","com.xueqiu.android:id/tab_name")
click_editgroup_loc=("id","com.xueqiu.android:id/edit_group")
click_managegroup_loc=("id","com.xueqiu.android:id/text")
click_creatgroup_loc=("id","com.xueqiu.android:id/add_item")
click_input_loc = ("id", "com.xueqiu.android:id/dialog_input_text")
click_confirm_loc = ("id", "com.xueqiu.android:id/bt_left")
driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
time.sleep(3)
text1=driver.find_elements_by_id("com.xueqiu.android:id/tab_name")
text1[1].click()

#print(driver. current_context)
#driver.background_app(2)
#text1=driver.find_element_by_xpath(u"//android.widget.TextView[@text='行情']").click()
time.sleep(3)
driver.quit()
"""



'''
data=read_caps()['start_loc']
print(data)
text1=driver.find_element(data[0],data[1])
print(text1)
'''
'''
driver.find_element_by_xpath(u"//android.widget.TextView[@text='行情']").click()
time.sleep(3)
driver.find_element_by_id("com.xueqiu.android:id/edit_group").click()
time.sleep(3)
driver.find_element_by_id("com.xueqiu.android:id/title2").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.EditText[@text='900']/../android.widget.ImageView").click()
time.sleep(3)
driver.find_element_by_id("com.xueqiu.android:id/tv_right").click()
time.sleep(3)
driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
text=driver.find_element_by_xpath("//android.widget.TextView[@text='900']")

print(text)

'''

driver.find_element_by_xpath(u"//android.widget.TextView[@text='行情']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.LinearLayout").click()
time.sleep(3)
'''
driver.find_element_by_xpath(u"//android.widget.TextView[@text='分时']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.TextView[@text='五日']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.TextView[@text='日K']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.TextView[@text='周K']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.TextView[@text='月K']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.TextView[@text='季K']").click()
time.sleep(3)
driver.find_element_by_xpath(u"//android.widget.TextView[@text='年K']").click()
time.sleep(3)
'''
for i in range(20):
    print("第%d次"%i)
    driver.find_element_by_xpath(u"//android.widget.TextView[@text='讨论']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//android.widget.TextView[@text='新帖']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//android.widget.TextView[@text='推荐']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//android.widget.LinearLayout[@resource-id='com.xueqiu.android:id/ll_title_content']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//android.widget.ImageView[@resource-id='com.xueqiu.android:id/arrow_right']").click()

driver.quit()
