import uiautomator2 as u2
import config

# 查看手机IP，然后通过IP连接，默认的端口7912
# 查看端口adb forward --list
device = u2.connect(config.DEVICE_NAME)
# 同理
# u2.connect_wifi("192.168.1.3")
print("wifi device = " + str(device))

# adb查看序列号
# device = u2.connect("38f38fd")
# print("serial device = " + str(device))
