import allure

from base.base import Base
import page


@allure.step(title="进入登录页面")
class Login(Base):
    @allure.step(title="进入登录操作")
    def login(self,name="18697780270",passwd="123321ly"):
        #账号登录，输入账号，密码
        allure.attach("账号", "{}".format(name))
        self.input_element(page.login_name_id,name)
        allure.attach("密码", "{}".format(passwd))
        self.input_element(page.login_passwd_id,passwd)
        allure.attach("点击登录按钮", "")
        self.click_element(page.login_btn_id)
    @allure.step(title="判断登录按钮是否存在")
    def login_btn(self):
        #判断登录按钮是否存在
        try:

            self.seach_element(page.login_btn_id)
            allure.attach("状态","存在")
            return True
        except:
            allure.attach("状态", "不存在")
            return False

    @allure.step(title="点击退出登录页面按钮")
    def click_close_log(self):
        # 点击登录页面退出按钮
        self.click_element(page.login_close_id)