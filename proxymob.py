import time

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

server = Server("C:/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# Начинаем захват сетевых запросов
proxy.new_har("form_data")
driver.get("https://ruforms.online/login")
time.sleep(5)
email_input = driver.find_element(By.NAME, 'email')
pass_input = driver.find_element(By.NAME, 'password')
sendBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
email = ''
password = ''
email_input.send_keys(email)
pass_input.send_keys(password)
sendBtn.click()
driver.get('https://ruforms.online/formAnswer/1efac8a2-ae32-67b6-b0dc-cecff9414307')
time.sleep(5)
har_data = proxy.har
for entry in har_data['log']['entries']:
     if entry['request']['url'] == 'https://ruforms.online/formAnswer':
          print(entry['request'])
          print(entry['response'])
time.sleep(1000)