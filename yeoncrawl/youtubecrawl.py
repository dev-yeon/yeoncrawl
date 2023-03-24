import warnings
import pandas as pd
from IPython.display import display
from selenium.webdriver.common.keys import Keys
warnings.filterwarnings(action='ignore')
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from requests import get



def read_video(youtube_video):
    return youtube_video

def get_video(request):

    feature = input('검색어를 입력하시오 : ')
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    url = " https://www.youtube.com/results?search_query="
    driver.get('https://www.youtube.com')

    n = 3
    while n > 0:
        print('웹페이지를 불러오는 중입니다..' + '..' * n)
        time.sleep(1)
        n -= 1

    src = driver.find_element_by_xpath('//*[@id="search"]')
    src.send_keys(feature)
    src.send_keys(Keys.RETURN)

    n = 2
    while n > 0:
        print('검색 결과를 불러오는 중 입니다..' + '..' * n)
        time.sleep(1)
        n -= 1

    print('데이터 수집 중 입니다....')

    html = driver.page_source
    soup = BeautifulSoup(html)

    df_title = []
    df_link = []
    df_writer = []
    df_view = []
    df_date = []

    for i in range(len(soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated'))):
        title = soup.find_all('a', {'id': 'video-title'})[i].text.replace('\n', '')
        link = 'https://www.youtube.com/' + soup.find_all('a', {'id': 'video-title'})[i]['href']
        writer = \
        soup.find_all('ytd-channel-name', 'long-byline style-scope ytd-video-renderer')[i].text.replace('\n', '').split(
            ' ')[0]
        view = \
        soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated')[i].text.split('•')[
            1].split('\n')[3]
        date = \
        soup.find_all('ytd-video-meta-block', 'style-scope ytd-video-renderer byline-separated')[i].text.split('•')[
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

    """

    result = input('데이터프레임 저장이 완료 되었습니다! 데이터프레임을 조회 하시겠습니까? (y/n)')
    if result == 'y':
        display(df_just_video)
        question = input('원하는 영상을 재생 하시겠습니까? (y/n)')
        if question == 'y':
            button = int(input('재생 하고자 하는 영상의 번호(출력된 표 가장 왼쪽의 번호)를 입력 해주세요.'))
            driver = webdriver.Chrome()
            driver.get(df_just_video['영상url'][button])
        else:
            return '프로그램 을 종료 합니다.'
    else:
        return '프로그램 을 종료 합니다.'
"""