import time
from selenium.webdriver.common.by import By
from selenium import webdriver

with open('./data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # 创建 Edge 浏览器驱动实例
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("http://www.bing.com")
        time.sleep(5)
        #登录
        driver.find_element(By.ID, 'id_p').click()
        driver.find_element(By.ID,'sb_form_q').send_keys(line)
        #driver.find_element(By.ID,'search_icon').click()
        time.sleep(5)


        # 关闭
        driver.quit()







