# Selenium Web Automation, Login into facebook
# Author : Joel Otepa Wembo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "joelotepawembo40@hotmail.com"
password = "JoelWembo@1234"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)

element.close()