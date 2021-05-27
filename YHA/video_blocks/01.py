import platform
import re
import subprocess

import win32api
import win32con


def getScreenDimensions():
    sysstr = platform.system()
    if sysstr == 'Windows':
        return win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    elif sysstr == 'Linux':
        xrandrOutput = str(subprocess.Popen(['xrandr'], stdout=subprocess.PIPE).communicate()[0])
        matchObj = re.findall(r'current\s(\d+) x (\d+)', xrandrOutput)
        if matchObj:
            return int(matchObj[0][0]), int(matchObj[0][1])
    else:
        return 1920, 1080


scr_width, scr_height = getScreenDimensions()
print(scr_width, scr_height)
