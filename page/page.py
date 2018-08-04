from page.index_home import Index_home
from page.sigin import Sigin
from page.login import Login
from page.huiyuan import Huiyuan
from page.seting_page import Seting_page
class Page():
    def __init__(self,driver):
        self.driver = driver
    def get_index_obj(self):
        return Index_home(self.driver)
    def get_sin_obj(self):
        return Sigin(self.driver)
    def get_log_obj(self):
        return Login(self.driver)
    def get_huiyuan_obj(self):
        return Huiyuan(self.driver)
    def get_seting_obj(self):
        return Seting_page(self.driver)