#a1qc_47

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.ozon.ru/")
time.sleep(5)
btn = driver.find_element(By.ID, 'reload-button')
btn.click()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME, "a1qc_47")
action = ActionChains(driver)
action.move_to_element(element).perform()

time.sleep(10000)

