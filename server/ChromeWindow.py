from selenium import webdriver
import chromedriver_binary             # パスを通すためのコード
import time
from selenium.webdriver.chrome.options import Options

options = Options()
# 現在開いてるChromeにたいしてSeleniumを当てるためのオプション
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# 上記のオプションを付与したWebDriverの作成
driver = webdriver.Chrome(options=options)

"""
シリアル通信によって送られてきたURLをChromeで開く

@param string url
"""


def openUrl(url):
    driver.get(url)


"""
現在アクティブになっているChromeのURLのTabを取得する

@param null
@return string active_url
"""


def getCurrentUrl():
    active_url = driver.current_url
    print(active_url)
