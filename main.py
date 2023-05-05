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

def get_items_urls(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            src = file.read()
    except FileNotFoundError:
        return "[ERROR] File not found!"
    except Exception as e:
        return f"[ERROR] Failed to open file: {e}"

    urls = []
    for line in src.split('\n'):
        href_index = line.find('href="')
        if href_index != -1:
            url_start = href_index + len('href="')
            url_end = line.find('"', url_start)
            if url_end != -1:
                url = line[url_start:url_end]
                urls.append(url)

    try:
        with open('items_urls.txt', 'w', encoding='utf-8') as file:
            for url in urls:
                file.write(f"{url}\n")
    except Exception as e:
        return f"[ERROR] Failed to write urls to file: {e}"

    return "[INFO] URLs collected successfully!"

def main():
    #get_source_html(url='https://careerspace.app/')
    print(get_items_urls(file_path='ver1.html'))

if __name__=="__main__":
    main()