from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 截图并将其保存到当前目录
def take_screenshot(driver, name="screenshot"):
    current_path = os.getcwd()
    screenshot_path = os.path.join(current_path, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

#登录
def CoreLogin(driver, username, password):
    try:
        driver.get('https://dppcoret.linksfield.net/')
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/div/div/form/button").click()
    except Exception as e:
        take_screenshot(driver, "login_error")
        raise e

def CoreMNOManager(driver):
    try:
        driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[2]/a/span[1]').click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'MNO Manager').click()
        time.sleep(7)
        iframe1ele = driver.find_element(By.NAME, 'iframe3')
        driver.switch_to.frame(iframe1ele)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'form-control').send_keys('pm')
        driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div[1]/div[4]/div/div[1]/button").click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="MnoTable"]/tbody/tr/td[1]/input').click()
        driver.find_element(By.XPATH, '//*[@id="MnoTableToolbar"]/button[4]').click()
        time.sleep(10)
        iframe2ele = driver.find_element(By.NAME, 'layui-layer-iframe1')
        driver.switch_to.frame(iframe2ele)
        driver.find_element(By.XPATH, '//*[@id="ensure"]').click()
        time.sleep(3)
    except Exception as e:
        take_screenshot(driver, "mno_manager_error")
        raise e

# 初始化
service = Service('C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20) # 显示wait
driver.maximize_window()


if __name__ == "__main__":
    try:
        CoreLogin(driver, 'admin', 'happy!123456')
        CoreMNOManager(driver)
    finally:
        driver.quit()
