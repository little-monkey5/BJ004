from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    # 初始化
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = '.umanager.LoginActivity'
        # 声明driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 查找元素  location为元组或列表， 且一定要返回
    def base_find(self, location, timeout=30, poll=0.5):
       return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*location))

    # 输入方法
    def base_input(self,location,text):
        # 获取元素
        ele = self.base_find(location)
        # 清空
        ele.clear()
        # 输入
        ele.send_keys(text)

    # 点击方法
    def base_click(self,location):
        # 获取元素
        self.base_find(location).click()

