from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

cookies = driver.get_cookies()
print(cookies)

driver.add_cookie({'name': 'my_cookie', 'value': 'cookie_value'})
cookies = driver.get_cookies()
print(cookies)

driver.delete_cookie('my_cookie')
cookies = driver.get_cookies()
print(cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(cookies)

time.sleep(10000)