
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
from django.http import HttpResponse


def read_video(video):
    return video
"""
def scroll_youtube():
    # 스크롤 높이 가져옴
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 끝까지 스크롤 내리기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 대기
        time.sleep(3)
        # 스크롤 내린 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
"""

def crawlyoutube(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # 유튜브에 검색하면 뜨는 정보를 selenium 으로 모사하기 위해서 driver.get  방식으로 불러온다


    base_url = "https://www.youtube.com/results?search_query=%ED%9D%AC%EB%A7%9D"
    #keyword = input('검색어를 입력하시오 : ')
    #driver.get(f"{base_url}{keyword}")
    driver.get(base_url)
    # 너무 많은 요청을 한번에 불러오면 차단당하니 슬립걸어주기
    time.sleep(3)

    you_html = driver.page_source
    you_soup = BeautifulSoup(you_html, "html.parser")
    videos = you_soup.select('div', "dismissible.style-scope.ytd-video-renderer")
    # 'div#dismissible.style-scope.ytd-video-renderer' 라는 형식 으로 유튜브 의 비디오 목록 들은 구성 되어 있다.
    results = []
    # 내가 넣은 유튜브 의 각각 값을 딕셔 너리 로 넣을 result 를 for 문 외부에 넣는다.
    # 크롬 우클릭 -> 검사-> 크롤링 할 해당 아이템 찾기-> copy ->copy XPath ..
    # XPath 를 어디 VSC, Sublime text 같은데 적어 둔다.

    for i, video in enumerate(videos):  # i는 0 부터 시작 한다. items 개별 항목들 각각의 item 에 숫자를 각각 붙여 준다.
        new_video = read_video(video)
        y_xpath = f'//*[@id="contents"]/ytd-rich-grid-row[{i+1}]/a'  # 이게 아까 복사한 XPath , 규칙성 이 보인다.
        y_button = driver.find_element(By.XPATH, y_xpath)
        #y_button.click()
        time.sleep(2)
        y_video_html = driver.page_source
        y_video_soup = BeautifulSoup(y_video_html, "html.parser")

        #src = driver.find_element(By.XPATH, y_xpath)
        #src.send_keys(keyword)
        #src.send_keys(Keys.RETURN)


        # you_html= driver.page_source
        # you_soup = BeautifulSoup(you_html, "html.parser")
        time.sleep(1)
        new_video_title = y_video_soup.find('', id='')
        new_video_writer = y_video_soup.find('', id='')
        new_video_link = y_video_soup.find('', id='')
        new_video_viewcount = y_video_soup.find('', id='')
        new_video_vdate = y_video_soup.find('', id='')

        video_data = {
            'new_video_title': new_video_title.text.strip(),
            'new_video_writer': new_video_writer.text.strip(),
            'new_video_link': new_video_link.text.strip(),
            'new_video_viewcount': new_video_viewcount.text.strip(),
            'new_video_vdate': new_video_vdate.text.strip()

        }
        print(video_data)
        time.sleep(1)
        results.append(video_data)
    print("crawl start")
    print(results)
    return HttpResponse("crawl Done! ")


