from time import sleep

import pytest
from selenium.webdriver.common.by import By

from base.init_driver import init_driver
from base.base import Base


drive=init_driver("com.android.browser",".BrowserActivity")
ba_obj = Base(drive)
ba_obj.click_element((By.ID,"com.android.browser:id/url"))
ba_obj.input_element((By.ID,"com.android.browser:id/url"),"www.baidu.com")
ba_obj.drive.keyevent(66)
print(ba_obj.drive.contexts)
ba_obj.drive.switch_to.context('WEBVIEW_com.android.browser')
# print(ba_obj.drive.page_source)
ba_obj.input_element((By.ID,"index-kw"),"123")
ba_obj.click_element((By.ID,"index-bn"))
sleep(5)
ba_obj.drive.quit()






