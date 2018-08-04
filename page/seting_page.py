import time

import allure

from base.base import Base
import page
@allure.step(title="进入设置页面")
class Seting_page(Base):
    @allure.step(title="执行退出操作")
    def outlog(self,tag=1):
        """
        退出登录
        :param tag: tag=1 确认退出 tag = 0 取消退出
        :return:
        """
        time.sleep(3)
        allure.attach("滑动操作", "屏幕向上滑动")
        self.swipe(0.5,0.8,0.5,0.3)
        allure.attach("退出操作", "点击退出")
        self.click_element(page.logout_btn_id)
        if tag:
            allure.attach("退出操作", "确认退出")
            self.click_element(page.confirm_logout_btn_id)