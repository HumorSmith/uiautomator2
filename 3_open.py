import uiautomator2 as u2
device = u2.connect("38f38fd")
device.app_start("com.ifreedomer.lovewallpaper")
device.app_stop("com.ifreedomer.lovewallpaper")
device.app_clear("com.ifreedomer.lovewallpaper")


