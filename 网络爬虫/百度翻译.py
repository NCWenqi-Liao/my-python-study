# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# item = input("请输入要翻译的内容")
# driver = webdriver.Edge()
# driver.get("https://fanyi.baidu.com/?aldtype=16047&ext_channel=Aldtype#auto/zh")
# driver.maximize_window()#最大化窗口
# driver.find_element(By.CSS_SELECTOR,".app-guide-close").click()
# time.sleep(3)
# driver.find_element(By.ID,"baidu_translate_input").click()
# driver.find_element(By.ID,"baidu_translate_input").send_keys(item)
# time.sleep(1)
# tra = driver.find_element(By.CSS_SELECTOR,"#cont-hanying")
# print(tra.text)


#当当网


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.get('https://www.dangdang.com/')
driver.find_element(By.CSS_SELECTOR,"#key_S").click()
driver.find_element(By.CSS_SELECTOR,"#key_S").send_keys('python')
driver.find_element(By.XPATH,'//*[@id="form_search_new"]/input[10]').click()
pr = driver.find_elements(By.CSS_SELECTOR,"shoplist li")
time.sleep(2)
