# from selenium import webdriver
# import chromedriver_binary             # パスを通すためのコード
# import time


# # time.sleep(10)
# #ChromeDriverのパスを引数に指定しChromeを起動
# driver = webdriver.Chrome()
# #指定したURLに遷移
# driver.get("https://www.google.co.jp")
# #カレントページのURLを取得
# cur_url = driver.current_url
# #カレントページのURLを表示
# print(cur_url)

 # -*- coding: utf-8 -*-
import pyautogui
#os系
import re
import os
import subprocess
import sys
import time
import array
#win32系
import win32gui
import win32con 
import time
time.sleep(2)

a =win32gui.GetWindowText (win32gui.GetForegroundWindow()) 
print(a)
