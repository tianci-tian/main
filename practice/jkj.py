import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# 设置 ChromeDriver 驱动路径
chrome_driver_path = r'C:\Users\huauyu\AppData\Local\Programs\Python\Python39\chromedriver.exe'


# 创建 Chrome 浏览器选项
options = ChromeOptions()
# 在这里可以设置 Chrome 浏览器的选项，例如启用或禁用某些功能
#options.add_argument("--incognito")  # 启用无痕模式

# 创建 Chrome 浏览器服务
service = Service(executable_path=chrome_driver_path)

# 使用选项和服务启动 Chrome 浏览器
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Chrome()
#最大化窗口
driver.maximize_window()
# 打开网站
driver.get("http://zhfytest.thunisoft.com:8428/spxt/artery/parse.do?action=parse&formId=f73995f55105b31de791bd59f72bc2f7&rtt=display###")
#等待两秒钟
time.sleep(2)
#定位下拉列表
dropdown_element = driver.find_element(By.ID, 'sp_mousedown1')
# 执行点击操作
dropdown_element.click()
#定位下拉列表 dropdown_element = driver.find_element(By.ID, 'sp_mousedown1') .click()这样也行
#选择北京市高级人民法院并点击
dropdown_element = driver.find_element(By.ID, '1') .click()
#定位输入框（用户名）
dropdown_element = driver.find_element(By.ID, 'usernametextfm1')
#输入用户名limeimei
dropdown_element.send_keys("limeimei")
#显示等待的方法定位密码输入框
#wait = WebDriverWait(driver, 10)
#dropdown_element = wait.until(EC.element_to_be_clickable((By.ID, 'passwordfm1')))
#定位输入框（密码）
#time.sleep(2)
#输入密码被js控制了，需要用ac高级事件对象处理
ac  = ActionChains(driver)

dropdown_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/dl/dd/form[1]/div[5]/div/input[1]")
#time.sleep(2)
#输入密码123456123456

dropdown_element.click()
ac.click().send_keys_to_element(dropdown_element,"123456123456").perform()

#点击登录
dropdown_element = driver.find_element(By.ID, 'btnLoad') .click()
time.sleep(5)
# 关闭浏览器
driver.qu