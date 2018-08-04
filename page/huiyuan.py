from base.base import Base
import page,allure
@allure.step(title="进入会员中心页")
class Huiyuan(Base):
    @allure.step(title="判断全部订单是否存在")
    def if_all_in_page(self):
        try:
            self.seach_element(page.all_order_xpath)
            allure.attach("状态","存在")
            return True
        except:
            allure.attach("状态", "不存在")
            return False
    @allure.step(title="点击设置按钮")
    def click_seting(self):
        self.click_element(page.setting_btn_id)