import config
import uiautomator2 as u2

device = u2.connect(config.DEVICE_NAME)
# device(text="笑面如花").click()
# device(resourceId="com.ifreedomer.lovewallpaper:id/pic_name_tv", text="笑面如花").click()
# device(resourceId="com.ifreedomer.lovewallpaper:id/pic_name_tv", instance=0).click()
device(resourceId="com.ifreedomer.lovewallpaper:id/item_hot").child(
    resourceId="com.ifreedomer.lovewallpaper:id/icon").click()
# 对象是否存在
exist = device(resourceId="aaaa").exists
