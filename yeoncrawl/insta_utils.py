from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import metadata
from django.http import HttpResponse


def driver(request):
    chrome_options = Options()
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver


def instagram_login(request):
    is_login_done = False
    # 인스타그램 접속
    driver(request).get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    # 로그인
    username = 'snobx0x'
    time.sleep(1)
    password = 'qwer12134'
    time.sleep(1)
    login = driver(request).find_element(By.NAME, "username")
    login.send_keys(username)
    driver(request).find_element(By.NAME, 'password').send_keys(password)
    driver(request).find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    time.sleep(3)
    is_login_done = True
    return is_login_done
