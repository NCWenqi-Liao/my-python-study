from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#from selenium import webdriver

driver = webdriver.Edge()


driver.get('https://www.12306.cn/index/')

driver.find_element(By.ID, 'fromStationText').click()
driver.find_element(By.ID, 'fromStationText').clear()
driver.find_element(By.ID, 'fromStationText').send_keys('新余'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[1]/div/div').click()

#
#
driver.find_element(By.ID, 'toStationText').click()
driver.find_element(By.ID, 'toStationText').clear()
driver.find_element(By.ID, 'toStationText').send_keys('南昌'+Keys.ENTER)
driver.find_element(By.ID, 'train_date').click()
driver.find_element(By.ID, 'train_date').clear()
driver.find_element(By.ID, 'train_date').send_keys('2024-03-21'+Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[1]/div/div').click()
driver.find_element(By.CSS_SELECTOR, '#search_one').click()
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="t-list"]/div[2]/a/span').click()

time.sleep(3)




input('......')