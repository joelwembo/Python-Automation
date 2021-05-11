from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=PATH)
driver.get("https://www.google.com/")
data = driver.page_source
print(data)
f= open("test.html","w+")
f.write(data)
time.sleep(1)

driver.save_screenshot('screenshot.png')

driver.quit()