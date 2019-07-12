from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.vcooline.aike'
desired_caps['appActivity'] = '.umanager.LoginActivity'
# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 定位用户名
driver.find_element_by_id("com.vcooline.aike:id/etxt_username").send_keys("13311111111")
# 定位密码
driver.find_element_by_id("com.vcooline.aike:id/etxt_pwd").send_keys("111111")
# 定位登录按钮
driver.find_element_by_id("com.vcooline.aike:id/btn_login").click()
