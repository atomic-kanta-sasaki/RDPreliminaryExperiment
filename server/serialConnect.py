import serial
import time

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


def serial_send():
    time.sleep(10)
    string = "hello windows"
    string += "\r\n"
    string = string.encode()
    ser.write(string)

    ser.close()
