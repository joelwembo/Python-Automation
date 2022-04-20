#Implementation of Selenium WebDriver with Python using PyTest
 
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()
    
    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()
 
    chrome_driver.find_element_by_name("li1").click()
    chrome_driver.find_element_by_name("li2").click()
 
    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title
 
    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element_by_id("sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)
 
    chrome_driver.find_element_by_id("addbutton").click()
    sleep(5)
