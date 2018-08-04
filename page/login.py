from base.base import Base
import page
class Login(Base):
    def login(self,name,passwd):
        #账号登录，输入账号，密码
        self.input_element(page.login_name_id,name)
        self.input_element(page.login_passwd_id,passwd)
        self.click_element(page.login_btn_id)
    def login_btn(self):
        #判断登录按钮是否存在
        try:
            self.seach_element(page.login_btn_id)
            return True
        except:
            return False
    def click_close_log(self):
        # 点击登录页面退出按钮
        self.click_element(page.login_close_id)