import pytest

import config
import uiautomator2 as u2
@pytest.mark.empty
def test_login_empty():
    d = u2.connect(config.DEVICE_NAME)
    d.app_stop("com.ifreedomer.lovewallpaper")
    d.app_start("com.ifreedomer.lovewallpaper")
    d(text="我的", resourceId="com.ifreedomer.lovewallpaper:id/smallLabel").click()
    d(text="注册/登录").click()
    d(resourceId="com.ifreedomer.lovewallpaper:id/accountEt").send_keys(" ")
    d(resourceId="com.ifreedomer.lovewallpaper:id/passwordEt").send_keys(" ")
    d(resourceId="com.ifreedomer.lovewallpaper:id/loginBtn").click()
    message = d.toast.get_message()
    assert "错误" in message


@pytest.mark.success
def test_login_not_emtpy():
    assert True


# if __name__ == '__main__':
# 命令行执行 pytest -m empty --html report.html
#     pytest.main(["-m empty"])
