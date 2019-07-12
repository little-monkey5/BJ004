import pytest
import os
import sys
sys.path.append(os.getcwd())
from v4.page.page_login import PageLogin

def get_data():
    return [("13800001111","123456"),("13800001112","123455")]

class TestLogin(object):
    # 初始化
    def setup_class(self):
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试用例
    @pytest.mark.parametrize("phone,pwd",get_data())
    def test_login(self,phone,pwd):
        self.login.page_login(phone,pwd)
# print(__name__)
if __name__ == '__main__':
    pytest.main("-s test_login.py")