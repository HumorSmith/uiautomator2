import uiautomator2 as u2

device = u2.connect("38f38fd")
print(device.app_current())
# adb shell dumpsys activity top | grep ACTIVITY
print(device.app_list_running())
# aapt dump badging hh.apk 查看apk的包名


