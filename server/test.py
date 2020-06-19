# import sys

# if sys.platform == "darwin":
#        import applescript
#        from AppKit import NSWorkspace
#        from Quartz import (
#            CGWindowListCopyWindowInfo,
#            kCGWindowListOptionOnScreenOnly,
#            kCGNullWindowID
#        )

# print(sys.platform)
import psutil
import os
import subprocess
import sys
from AppKit import NSWorkspace
import time
from Foundation import *
import applescript

os.getpid()
p = psutil.Process(os.getpid())
print(p)
p.name()
print(p.name)
p.exe()
print(p.cmdline)
p.cmdline()

print("===============================================")
# pid = subprocess.check_output(["xdotool", "getactivewindow", "getwindowpid"]).decode("utf-8").strip()

# print(pid)

print(sys.platform)

t = range(1,100)
for i in t:
    time.sleep(3)
    # Macのアクティブモニタを取得することができる
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    # 取得したアクティブモニタを利用して例えば, ChromeならURLファイルならファイルパスを使用してBluetoothなどでそのファイルを転送するプログラムを記述
    # あとはPC上で動いているプログラムとスマートウォッチ上で動かすファイルの組み込み的なことをする
    print(activeAppName)
    r = applescript.tell.app("Terminal", 'do script "osascript -e \'tell app "google chrome" to get the url of the active tab of window 1\'"')
    print(r)