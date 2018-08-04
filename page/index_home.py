from base.base import Base
import page,allure


@allure.step(title="进入首次展示页面")
class Index_home(Base):
    @allure.step(title="点击我")
    def click_my_btn(self):
        self.click_element(page.my_btn_id)