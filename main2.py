#https://ya.ru/
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver

def open_page_and_wait(driver, url):
    driver.get(url)
    # searchInput = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.NAME, "text"))
    # )
    # search_word = "Купить айфон"
    # for char in search_word:
    #     searchInput.send_keys(char)
    #     time.sleep(0.1)
    # suggest__button = driver.find_element(By.CLASS_NAME, 'mini-suggest__button')
    # suggest__button.click()
    # links = WebDriverWait(driver, 60).until(
    #     EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
    # )
    # print(links)
    # while True:
    #     linkFind = False
    #     time.sleep(5)
    #     links = WebDriverWait(driver, 60).until(
    #         EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
    #     )
    #     if not linkFind:
    #         try:
    #             for link in links:
    #                 if "https://www.apple.com/iphone/" in link.get_attribute("href"):
    #                     linkFind = True
    #                     link.click()
    #             if not linkFind:
    #                 time.sleep(5)
    #                 pnnext = driver.find_element(By.CLASS_NAME, 'Pager-Item_type_next')
    #                 pnnext.click()
    #             else: break
    #         except Exception as e:
    #             print(e)
    time.sleep(10)
    titles = WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-tile-headline'))
            )

    for title in titles:
        print(title.text)

browser = start_browser()
open_page_and_wait(browser, "https://www.apple.com/iphone/")
