'''
原文地址：
https://mp.weixin.qq.com/s?__biz=MzUxMTA3NzgzMQ==&mid=2247561395&idx=1&sn=e60843b9ede8bce211f8e8fa0bad098d&chksm=f87dfb8800e779ae24d521035609bfd8ae3b95e59708074a6773d452b3d0cc94862c6139b9dc&mpshare=1&scene=2&srcid=1015PQb9jlsOwoIfPhhue0mj&sharer_shareinfo=03b135ea2afc78e121ed29a84f057adc&sharer_shareinfo_first=bcd6467d5721af5c9c094e4dd332a0c8#rd

运行测试：
方法一：在项目根目录下运行 behave 命令，执行测试：
    PS D:\workspace_pycharm\my_bdd_project> behave
方法二：可以在tests目录下新建test_runner.py文件:
    再执行命令：python tests/test_runner.py
'''



from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('用户在登录页面')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://example.com/login')

@when('用户输入有效的用户名和密码')
def step_when_user_enters_valid_credentials(context):
    context.driver.find_element(By.ID, 'username').send_keys('valid_username')
    context.driver.find_element(By.ID, 'password').send_keys('valid_password')
    context.driver.find_element(By.ID, 'submit').click()

@then('用户应看到主页')
def step_then_user_should_see_home_page(context):
    assert 'Home' in context.driver.title

@when('用户输入无效的用户名和密码')
def step_when_user_enters_invalid_credentials(context):
    context.driver.find_element(By.ID, 'username').send_keys('invalid_username')
    context.driver.find_element(By.ID, 'password').send_keys('invalid_password')
    context.driver.find_element(By.ID, 'submit').click()

@then('用户应看到错误消息')
def step_then_user_should_see_error_message(context):
    error_message = context.driver.find_element(By.ID, 'error').text
    assert 'Invalid username or password' in error_message






