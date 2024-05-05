from selenium import webdriver
from selenium.webdriver.common.by import By
import time
account = '18879072710'
password = 'Lwq20050612'
my_idcard = '4433'


# 创建一个Chrome浏览器实例
driver = webdriver.Edge()

# 打开12306的登录页面
driver.get("https://kyfw.12306.cn/otn/resources/login.html")

# 等待一段时间，确保页面加载完成


# 定位用户名和密码输入框，并输入相应的信息
driver.find_element(By.ID, 'J-userName').send_keys(account)
driver.find_element(By.ID, 'J-password').send_keys(password)
driver.find_element(By.ID, 'J-login').click()
#time.sleep(2)
driver.implicitly_wait(4)
driver.find_element(By.ID, 'id_card').send_keys(my_idcard)
driver.find_element(By.ID, 'verification_code').click()
comfirm_code = input('请输入验证码:')
#time.sleep(15)
driver.find_element(By.ID, 'code').send_keys(comfirm_code)
driver.find_element(By.ID, 'sureClick').click()
driver.find_element(By.ID, 'link_for_ticket').click()
input('...')
driver.quit()












