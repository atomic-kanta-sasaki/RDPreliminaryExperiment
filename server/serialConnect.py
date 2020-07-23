import serial
import time
import ChromeWindow

ser = serial.Serial('COM8', 9600, timeout=None)

"""
シリアル通信で送られてくるデータを取得する

@return line
"""


def serial_read():
    line = ser.readline()
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

serial_send(ChromeWindow.getCurrentUrl)


beContinue = True
while beContinue == True:
    recive_data = serial_read()
    print("send data")
    print(recive_data)
    if recive_data != "":
        print("get chrome link")
        send_data = ChromeWindow.getCurrentUrl()
        print("link")
        print(send_data)
        serial_send(send_data)
    else:
        ChromeWindow.openUrl(recive_data)