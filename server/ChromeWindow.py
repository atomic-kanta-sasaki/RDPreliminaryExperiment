from selenium import webdriver
import chromedriver_binary             # パスを通すためのコード
import time
from selenium.webdriver.chrome.options import Options


# # time.sleep(10)
# # ChromeDriverのパスを引数に指定しChromeを起動
# driver = webdriver.Chrome()
# # 指定したURLに遷移
# driver.get("https://www.google.co.jp")


# def getCurrentUrl():

#     cur_url = driver.current_url
#     # カレントページのURLを表示
#     print(cur_url)


# input = input()
# # カレントページのURLを取得
# if input != "":
#     print("入っては来ている")
#     getCurrentUrl()
# time.sleep(10)
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options)

# driver.get('https://teratail.com/questions/277418')


print(driver.current_url)
