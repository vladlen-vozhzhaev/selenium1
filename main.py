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
    try:
        q = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )
        search_word = "Купить айфон"
        for char in search_word:
            q.send_keys(char)
            time.sleep(0.1)

        btnK = driver.find_element(By.NAME, "btnK")
        btnK.click()
        while True:
            linkFind = False
            time.sleep(5)
            links = WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
            )
            if not linkFind:
                try:
                    for link in links:
                        print(link.get_attribute("href"))
                        if "https://moskva.istoreapple.ru/" in link.get_attribute("href"):
                            print("Ссылка найдена")
                            linkFind = True
                    if not linkFind:
                        time.sleep(5)
                        pnnext = driver.find_element(By.ID, 'pnnext')
                        pnnext.click()
                except Exception as e:
                    print(e)

    except Exception as e:
        print("Ошибка при ожидании страницы", e)

browser = start_browser()
open_page_and_wait(browser, "https://google.com")

time.sleep(10)