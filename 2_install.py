import uiautomator2 as u2

device = u2.connect("38f38fd")
device.app_install("https://www.chinesepast.com/apk/love_wallpaper_1.7.5.apk")
# 寻找文字进行点击,点击需要在开发者设置里面打开Usb调试允许模拟点击
# device(text='安卓壁纸精选').click()
# # 获取包名
# print(device.app_current())
# # 卸载
# device.app_uninstall("com.ifreedomer.lovewallpaper")
