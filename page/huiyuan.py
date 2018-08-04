from base.base import Base
import page
class Huiyuan(Base):
    def if_all_in_page(self):
        try:
            self.seach_element(page.all_order_xpath)
            return True
        except:
            return False

    def click_seting(self):
        self.click_element(page.setting_btn_id)