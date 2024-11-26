from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://ttt/")
# Перетаскиваемый элемент
source_element = driver.find_element(By.ID, 'drag')
# На который перетаскиваем
target_element = driver.find_element(By.ID, 'drop')
#
actions = ActionChains(driver)

actions.drag_and_drop(source_element, target_element).perform()

time.sleep(10000)