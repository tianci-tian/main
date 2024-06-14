import time
from selenium import webdriver

# 1.实例化启动对象

desired_caps = dict()
# 链接app五大参数
desired_caps['platformName'] = 'Android'  # 平台名称：Android/iOS
desired_caps['platformVersion'] = '5.1'  # 版本号：知道准确的尽量写准确的，不知道可以把5.2.1写成 5.1或5
desired_caps['devicesName'] = 'K5J0220313008474'  # 设备名称：使用adb devices查看
desired_caps['appPackage'] = 'com.android.settings'  # 包名：查看启动包名称
desired_caps['appActivity'] = '.Settings'  # 启动页名称：查看启动页名称

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# Remote是appium.webdriver的方法
# http://localhost:4723/wd/hub是固定值
'''
appium自动录制

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(597, 2326)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(611, 1389)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(853, 117)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(191, 1692)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(284, 965)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(970, 867)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(937, 466)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
'''


# 2.测试步骤

time.sleep(5)

# 3.关闭驱动对象
driver.quit()

'''

# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:platformVersion": "10",
	"appium:devicesName": "597a6696",
	"appium:appPackage": "com.android.settings",
	"appium:appActivity": "com.android.settings.SubSettings",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


driver.quit()
'''
