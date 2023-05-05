import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

def get_source_html(url):
    service = Service('chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(2)
        current_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == current_height:
                with open('ver1.html', 'w', encoding='utf-8') as file:
                    file.write(driver.page_source)
                break
            current_height = new_height
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_source_html(url='https://careerspace.app/')

if __name__=="__main__":
    main()