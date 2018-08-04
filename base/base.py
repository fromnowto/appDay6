from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.drive = driver
    def seach_element(self,loc,timeout=15,poll=1):
        """
        定位单个元素
        :param loc: 元组类型 如：（By.ID,id属性）
        :param timeout:超时时间
        :param poll: 搜索频率
        :return: 定位对象
        """
        return WebDriverWait(self.drive,timeout,poll).until(lambda x:x.find_element(*loc))
    def seach_elements(self,loc,timeout=15,poll=1):
        """
        定位一组元素
        :param loc: 元组类型 如：（By.ID,id属性）
        :param timeout:超时时间
        :param poll: 搜索频率
        :return: 定位对象
        """
        return WebDriverWait(self.drive,timeout,poll).until(lambda x:x.find_elements(*loc))
    def click_element(self,loc,timeout=15,poll=1):
        """
        点击单个元素
        :param loc: 元组类型 如：（By.ID,id属性）
        :param timeout:超时时间
        :param poll: 搜索频率
        :return:
        """
        self.seach_element(loc,timeout,poll).click()
    def input_element(self,loc,text,timeout=15,poll=1):
        """
           点击单个元素
           :param loc: 元组类型 如：（By.ID,id属性）
           :param text: 要输入的内容
           :param timeout:超时时间
           :param poll: 搜索频率
           :return:
         """
        ele=self.seach_element(loc, timeout, poll)
        ele.clear()
        ele.send_keys(text)
    def swipe(self,start_x,start_y,end_x,end_y):
        """
        滑动手机
        :param start_x: 屏幕的百分比
        :param start_y:屏幕的百分比
        :param end_x: 屏幕的百分比
        :param end_y: 屏幕的百分比
        :return:
        """
        x=self.drive.get_window_size().get("width")
        y=self.drive.get_window_size().get("height")
        self.drive.swipe(x*start_x,y*start_y,x*end_x,y*end_y)
    def get_taost(self,msge):
        st=self.seach_element((By.XPATH, "//*[contains(@text,'{}')]".format(msge)), timeout=5,poll=0.5)
        return st.text