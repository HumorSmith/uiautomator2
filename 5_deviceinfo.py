import uiautomator2 as u2
import config
device = u2.connect(config.DEVICE_NAME)
# 设备信息
print(device.info)
print(device.device_info)
print(device.window_size())
# 设备操作
# print(device.screenshot("test.png"))
# print(device.push("test.png", "/sdcard/test.png"))
# print(device.pull("/sdcard/test.png", "test1.png"))
