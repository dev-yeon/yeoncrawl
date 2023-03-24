import pandas as pd
from bs4 import BeautifulSoup
from django.contrib.gis.gdal import feature
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
from django.http import HttpResponse

def read_video(video):
    return video
def crawlyoutube(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # 유튜브에 검색하면 뜨는 정보를 selenium 으로 모사하기 위해서 driver.get  방식으로 불러온다
    base_url= "https://www.youtube.com/results?search_query="
    keyword = input('검색어를 입력하시오 : ')
    driver.get(f"{base_url}{keyword}")
    time.sleep(3)
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

    you_html = driver.page_source
    # BeautifulSoup로 html 을 다 불러 온다.
    you_soup = BeautifulSoup(you_html, "html.parser")
    videos = you_soup.select('div',  "dismissible.style-scope.ytd-video-renderer")
    # 'div#dismissible.style-scope.ytd-video-renderer' 라는 형식 으로 유튜브 의 비디오 목록 들은 구성 되어 있다.
    results = []
    # 내가 넣은 유튜브 의 각각 값을 딕셔 너리 로 넣을 result 를 for 문 외부에 넣는다.
    # 크롬 우클릭 -> 검사-> 크롤링 할 해당 아이템 찾기-> copy ->copy XPath ..
    # XPath 를 어디 VSC, Sublime text 같은데 적어 둔다.
    n = 3
    while n > 0:
        print('웹 페이지 를 불러오는 중 입니다..' + '..' * n)
        time.sleep(1)
        n -= 1
        for i, video in enumerate(videos):   # i는 0 부터 시작 한다. items 개별 항목들 각각의 item 에 숫자를 각각 붙여 준다.
            new_video = read_video(video)
            y_xpath = f'//*[@id="contents"]/ytd-rich-grid-row[i+1]/a'  # 이게 아까 복사한 XPath , 규칙성 이 보인다.
            y_button = driver.find_element(By.XPATH, y_xpath)
            y_button.click()
            time.sleep(2)
            y_video_html = driver.page_source
            y_video_soup = BeautifulSoup(y_video_html, "html.parser")

            src = driver.find_element(By.XPATH, y_xpath)
            src.send_keys(keyword)
            src.send_keys(Keys.RETURN)

    n = 2
    while n > 0:
        print('검색 결과를 불러 오는 중 입니다..' + '..' * n)
        time.sleep(1)
        n -= 1

    print(' 데이터 수집 중 입니다....')
    #you_html= driver.page_source
    # you_soup = BeautifulSoup(you_html, "html.parser")


    df_title = []
    df_link = []
    df_writer = []
    df_view = []
    df_date = []

    for i in range(len(you_soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated'))):
        title = you_soup.find_all('a', {'id': 'video-title'})[i].text.replace('\n', '')
        link = 'https://www.youtube.com/' + you_soup.find_all('a', {'id': 'video-title'})[i]['href']
        writer = \
            you_soup.find_all('ytd-channel-name', 'long-byline style-scope ytd-video-renderer')[i].text.replace('\n',
                                                                                                            '').split(
                ' ')[0]
        view = \
            you_soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated')[i].text.split('•')[
                1].split('\n')[3]
        date = \
            you_soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated')[i].text.split('•')[
                1].split('\n')[4]

        df_title.append(title)
        df_link.append(link)
        df_writer.append(writer)
        df_view.append(view)
        df_date.append(date)

    df_just_video = pd.DataFrame(columns=['영상제목', '채널명', '영상url', '조회수', '영상등록날짜'])

    df_just_video['영상제목'] = df_title
    df_just_video['채널명'] = df_writer
    df_just_video['영상url'] = df_link
    df_just_video['조회수'] = df_view
    df_just_video['영상등록날짜'] = df_date

    df_just_video.to_csv('../data/df_just_video.csv', encoding='utf-8-sig', index=False)

    driver.close()

    # 너무많은 요청을 한번에 불러오면 내 url을 차단 할 수 있어서, 3초간 슬립을 걸어준다.
    time.sleep(3)





