from selenium import webdriver
import chromedriver_binary             # パスを通すためのコード
import time
from selenium.webdriver.chrome.options import Options
import serial

ser = serial.Serial('COM8', 9600, timeout=None)

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
    return active_url


"""
シリアル通信で送られてくるデータを取得する

@return line
"""
def serial_read():
    line = ser.readline(10000)
    print(line)
    ser.close()
    return line


"""
シリアル通信を用いてデータを送信する
"""
def serial_send(url):
    time.sleep(10)
    url = url.encode()
    ser.write(url)

    ser.close()

beContinue = True
while beContinue == True:
    print("loop start")
    recive_data = serial_read()
    print("send data")
    print(recive_data)
    if recive_data != "":
        print("get chrome link")
        send_data = getCurrentUrl()
        print("link")
        print(send_data)
        # serial_send(send_data)
    else:
        openUrl(recive_data)
ser.close()
print("-------------------------------------")