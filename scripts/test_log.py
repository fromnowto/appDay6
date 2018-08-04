import sys,os
sys.path.append(os.getcwd())
import allure


from base.get_datas import get_datas
from base.init_driver import init_driver
from page.page import Page
import pytest
def data_list():
    list1=[]
    data_dict = get_datas("log_data.yaml")
    for i in data_dict:
        list1.append((i,data_dict.get(i).get("name"),data_dict.get(i).get("passwd"),data_dict.get(i).get("tag"),
                      data_dict.get(i).get("get_mes"),data_dict.get(i).get("expect")))
    return list1

class Test_log():
    def setup_class(self):
        self.page_obj = Page(init_driver())
    def teardown_class(self):
        self.page_obj.driver.quit()
    @pytest.mark.parametrize("test_id,name,passwd,tag,redy,shiji",data_list())
    def test_lod(self,test_id,name,passwd,tag,redy,shiji):
        allure.attach("用例编号","{}".format(test_id))
        self.page_obj.get_index_obj().click_my_btn()
        self.page_obj.get_sin_obj().click_old_num()
        self.page_obj.get_log_obj().login(name,passwd)

        if tag:
            try:
                at = self.page_obj.get_huiyuan_obj().if_all_in_page()
                self.page_obj.get_huiyuan_obj().click_seting()
                self.page_obj.get_seting_obj().outlog()
                assert at

            except:
                self.page_obj.get_log_obj().click_close_log()
                assert False
        else:
            try:
                ast=self.page_obj.get_log_obj().get_taost(redy)
                log_butn=self.page_obj.get_log_obj().login_btn()

                assert ast == shiji and log_butn
            except:
                assert False

            finally:
                self.page_obj.get_log_obj().click_close_log()













if __name__ == '__main__':
     pytest.main("-s test_log.py")
