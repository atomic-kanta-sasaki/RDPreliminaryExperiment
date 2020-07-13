from selenium import webdriver
import chromedriver_binary             # パスを通すためのコード
import time


time.sleep(5)
#カレントページのURLを取得
cur_url = driver.current_url
#カレントページのURLを表示
print(cur_url)