from base.base import Base
import page
class Sigin(Base):
    def click_old_num(self):
        # 点击已有账号登录
        self.click_element(page.exits_account_id)