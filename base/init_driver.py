from appium import webdriver


"""def init_driver(adviy,doive):
    init_dict={}
    init_dict["platformName"] = "Android"
    init_dict["platformVersion"] = "5.1"
    init_dict["deviceName"] = "addid"
    init_dict["appPackage"] = adviy
    init_dict["appActivity"] = doive
    init_dict["unicodeKeyboard"] = True
    init_dict["resetKeyboard"] =True
    driver = webdriver.Remote("127.0.0.1:4723/wb/hub",init_dict)
    return driver"""
def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps["automationName"] ="Uiautomator2"

    desired_caps['appPackage'] = "com.yunmall.lc"
    desired_caps['appActivity'] = "com.yunmall.ymctoc.ui.activity.MainActivity"
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

