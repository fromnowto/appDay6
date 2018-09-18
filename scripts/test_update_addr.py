import sys,os
from time import sleep

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.init_driver import init_driver
from page.page import Page
import pytest
class Test_updata_addr:
    def setup_class(self):
        self.page_obj = Page(init_driver())
        self.page_obj.if_login()
    def teardowm_class(self):
        self.page_obj.driver.quit()
    def test_001(self):
        self.page_obj.get_huiyuan_obj().click_seting()
        self.page_obj.get_huiyuan_obj().click_element((By.XPATH,"//*[contains(@text,'地址管理')]"))
        # test=self.page_obj.get_huiyuan_obj().seach_elements((By.XPATH,"//*[contains(@text,'hello')]/following-sibling::*/*"))
        test=self.page_obj.get_huiyuan_obj().seach_elements((By.XPATH,"//*[contains(@text,'默认')]/../preceding-sibling::*"))
        for i in test:
            print(i.text)
        assert 1
if __name__ == '__main__':
    pytest.main("-s test_update_addr.py")
