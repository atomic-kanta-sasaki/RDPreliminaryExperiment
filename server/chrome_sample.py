from selenium import webdriver
import chromedriver_binary             # パスを通すためのコード
import time
from selenium.webdriver.chrome.options import Options
import serial

ser = serial.Serial('COM9', 9600, timeout=None)
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
    return line

"""
シリアル通信を用いてデータを送信する
"""
def serial_send(url):
    ser.write(url)

"""
シリアル通信で送られてきた文字列をノイズのない形に整形する
"""
def sentenceShaping(text):
    shaping_text = text.strip().decode('utf-8')
    print("整形後データ")
    print(shaping_text)
    return shaping_text

"""
取得した値がフラグか判断する
フラグの場合は数値型に変換する
条件：配列長さが3以下だったらフラグ、そうでなければURL

@param recive_data
"""
def checkReciveData(recive_data):
    if len(recive_data) <= 3:
        return int(recive_data)
    else:
        return recive_data

print("port is open")
beContinue = True
while beContinue == True:
    print("loop start")
    recive_data = serial_read()
    recive_data = sentenceShaping(recive_data)

    if checkReciveData(recive_data) == 1:
        print("get chrome link")
        send_data = getCurrentUrl()
        send_data = str(send_data) + "\r\n"
        serial_send(send_data.encode('utf-8'))
    else:
        print("open chrome")
        openUrl(recive_data)
ser.close()
print("-------------------------------------")
