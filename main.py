import requests
from bs4 import BeautifulSoup
from selenium import webdriver
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
                if '/job/' in url:
                    if not url.startswith('http'):
                        url = f'https://careerspace.app{url}'
                    urls.append(url)

    try:
        with open('items_urls.txt', 'w', encoding='utf-8') as file:
            for url in urls:
                file.write(f"{url}\n")
    except Exception as e:
        return f"[ERROR] Failed to write urls to file: {e}"

    return "[INFO] URLs collected successfully!"


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [url.strip() for url in file.readlines()]
        print(urls_list)
        for url in urls_list:
            response = requests.get(url=url)
            soup = BeautifulSoup(response.text, "lxml")

            try:
                title = soup.find("title").text.strip()
            except (AttributeError, TypeError) as ex:
                title = None
                print(f"Exception occurred: {ex}")

            try:
                vacancy = soup.find("h3", class_="cs-t--title28").text.strip()
            except AttributeError as ex:
                vacancy = None
                print(f"Exception occurred: {ex}")

            try:
                body = soup.find("div", class_="j-d-desc").text.strip()
            except AttributeError as ex:
                body = None
                print(f"Exception occurred: {ex}")

            try:
                company = soup.find("div", class_="j-d-h__company").text.strip()
            except AttributeError as ex:
                company = None
                print(f"Exception occurred: {ex}")

            try:

                job_info = []
                city_span = soup.find_all('span', class_='job-lb__tx')

                for span in city_span:
                    job_info.append(span.get_text(strip=True))

                city = []
                job_format = []
                for i in range(len(job_info)):
                    if job_info[i] == "Удаленно" or job_info[i] == "Гибрид":
                        job_format.append(job_info[i])
                    else:
                        city.append(job_info[i])

            except AttributeError as ex:
                job_format = None
                city = None
                print(f"AttributeError occurred: {ex}")

            try:
                salary = soup.find("span", class_="price").text.strip()
            except AttributeError as ex:
                salary = None
                print(f"AttributeError occurred: {ex}")

            results_dict = {
                'chat_name': 'https://careerspace.app/',
                'title': title,
                'body': body,
                'vacancy': vacancy,
                'vacancy_url': url,
                'company': company,
                'company_link': '',
                'english': None,
                'relocation': None,
                'job_type': job_format,
                'city': city,
                'salary': salary,
                'experience': '',
                'time_of_public': None,
                'contacts': None,
                # 'session': self.current_session
            }
            print(results_dict)


def main():
    get_source_html(url='https://careerspace.app/')
    print(get_items_urls(file_path='ver1.html'))
    get_data(file_path='items_urls.txt')


if __name__ == "__main__":
    main()
