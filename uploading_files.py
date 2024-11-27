from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ruforms.online/form/1efac8a2-ae32-67b6-b0dc-cecff9414307")
text_input = driver.find_element(By.NAME, 'r0')
text_input.send_keys("Test text")
radio_buttons = driver.find_elements(By.NAME, 'r1')
for btn in radio_buttons:
    if btn.get_attribute('value') == '2':
        btn.click()

upload_element = driver.find_element(By.NAME, 'r2')
file_path = "C:/Users/Asus/Desktop/p.pptx"
upload_element.send_keys(file_path)

sendBtn = driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
sendBtn.click()

time.sleep(1000)