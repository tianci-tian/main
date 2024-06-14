from selenium import webdriver  # webdriver浏览器驱动，包含了各种前端浏览器的操作的工具方法
from selenium.webdriver.common.by import By
driver =webdriver.Chrome()
driver.implicitly_wait(5) #隐式等待5s
driver.maximize_window()
driver.get("http://www.baidu.com")

#层级属性结合定位输入框
driver.find_element(By.XPATH,"//form[@id='form']/span/input[1]").send_keys('selenuim')
#ID定位“百度一下”
driver.find_element(By.ID, "su").click()
#关闭
driver.quit()












