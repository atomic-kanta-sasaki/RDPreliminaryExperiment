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
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    print(activeAppName)