from base.base import Base
import page
class Index_home(Base):
    def click_my_btn(self):
        self.click_element(page.my_btn_id)