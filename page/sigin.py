import allure

from base.base import Base
import page
@allure.step(title="进入注册页面")
class Sigin(Base):
    @allure.step(title="点击已有账号登录")
    def click_old_num(self):
        # 点击已有账号登录
        self.click_element(page.exits_account_id)