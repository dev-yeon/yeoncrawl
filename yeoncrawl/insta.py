from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import time

def insta_crawl(request):
    # 웹 드라이버 실행
    chrome_options = Options()
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # 인스타그램 접속
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    # 로그인
    username = 'snobx0x'
    time.sleep(1)
    password = 'qwer12134'
    login = driver.find_element(By.NAME, "username")
    login.send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    time.sleep(3)

    # 해시태그 검색
    hashtag = '팬케이크'
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(60)

    # 게시물 가져오기
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.select('article')

    for article in articles:
        # 게시물 정보 출력
        print(article.select_one('a')['href'])
        print(article.select_one('img')['src'])
        print(article.select_one('img')['alt'])

    # 웹 드라이버 종료
    driver.quit()