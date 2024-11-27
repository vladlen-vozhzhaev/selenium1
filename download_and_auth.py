import time
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyEventListener(AbstractEventListener):
    def before_click(self, element, driver):
        print(f"Before clicking on: {element}")
    def after_click(self, element, driver):
        print(f"Clicked on: {element}")
    def before_navigate_to(self, url, driver):
        print(f"About to navigate to: {url}")
    def after_navigate_to(self, url, driver):
        print(f"Navigated to: {url}")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 20.0
width = 1920
height = 1080
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

chrome_options = Options()
download_directory = "E:\selenuim_files"
chrome_options.add_experimental_option("prefs", {
    'download.default_directory': download_directory,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True
})
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

event_driver = EventFiringWebDriver(driver, MyEventListener())

event_driver.get("https://ruforms.online/login")
for _ in range(100):
    # Получение скриншота как строки байтов PNG
    png_data = event_driver.get_screenshot_as_png()

    # Декодирование изображения из строки байтов в массив NumPy
    np_img = np.frombuffer(png_data, dtype=np.uint8)
    img = cv2.imdecode(np_img, flags=cv2.IMREAD_COLOR)
    # Запись кадра в видеофайл
    out.write(img)

#driver.save_screenshot('s1.png')
email_input = event_driver.find_element(By.NAME, 'email')
pass_input = event_driver.find_element(By.NAME, 'password')
sendBtn = event_driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
email = ''
password = ''
email_input.send_keys(email)
pass_input.send_keys(password)
sendBtn.click()
event_driver.get('https://ruforms.online/formAnswer/1efac8a2-ae32-67b6-b0dc-cecff9414307')
out.release()
time.sleep(5)
#driver.save_screenshot('s2.png')
links = event_driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    if "/storage/form_files/" in link.get_attribute('href'):
        print('Начинаю скачивание')
        link.click()

time.sleep(1000)