import time

from base.base import Base
import page
class Seting_page(Base):
    def outlog(self,tag=1):
        """
        退出登录
        :param tag: tag=1 确认退出 tag = 0 取消退出
        :return:
        """
        time.sleep(3)
        self.swipe(0.5,0.8,0.5,0.3)
        self.click_element(page.logout_btn_id)
        if tag:
            self.click_element(page.confirm_logout_btn_id)