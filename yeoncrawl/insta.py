
from selenium.webdriver.common.by import By
import yeoncrawl.insta_utils
import yeoncrawl.metadata as metadata
from bs4 import BeautifulSoup
import time
from .models import Post, PostImg

def read_item(item):
    return item

# 인스타의 html 코드를 insta_soup 에 넣기
def insta_soup(request):
    # 웹 드라이버 실행
    #chrome_options = Options()
    #chrome_options.add_argument(
    #    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
   # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = yeoncrawl.insta_utils.driver(request)
    # 인스타그램 접속
    driver.get(metadata.LOGIN_URL)
    time.sleep(2)
    # 로그인
    """
    username = metadata.INSTAGRAM_ID
    time.sleep(1)
    password = metadata.INSTAGRAM_PW
    time.sleep(1)
    login = driver.find_element(By.NAME, "username")
    login.send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    time.sleep(3)
    """
    login = yeoncrawl.insta_utils.instagram_login(request)
    # 해시태그 검색
    driver.get(f"{metadata.CONTENT_URL}{metadata.HASH_TAG}/")
    time.sleep(60)
    # 게시물 가져오기
    item_soup = BeautifulSoup(driver.page_source, 'html.parser')
    #  articles = soup.select('article')
    items = item_soup.select('div._aabd._aa8k._al3l')
    # div._aabd._aa8k._al3l 라는 형식으로 인스타의 아이템들은 구성되어있다 .
    return item_soup

# 인기게시물 9개 읽기 (하드코딩)
def hayatteru_9(request):
    driver = yeoncrawl.insta_utils.driver(request)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                i_path = f'//*[@id="mount_0_0_fC"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[{i}]/div/div/div[{j}]/div[{k}]'
                i_button = driver.find_element(By.XPATH, i_path)
                i_button.click()
                time.sleep(3)
                temp_post = Post()  # models 의 Post 호출
                temp_post.save() #한번 세이브해서 일단 Post db에 새로운 데이터 생성
                #------------------------
                temp_postimg = PostImg()  # 새로운 이미지 저장할 그릇 생성
                temp_postimg.img_url = ['srcset', 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']
                temp_postimg.save()
                temp_post.img_list.add(temp_postimg)
                temp_post.save()
                count = 0
                count = count+i  #  총 저장 갯수를 저장하는 변수 count가 있다. 이 count는 9개를 읽으면 [i] [j] [k]에서
                if (k==4):      # count  가 4 가 되면, k를 1로 초기화 한다.
                    k ==1
                    continue    # for문 밖으로 빠져나온다







            # <img> 태그의 alt 속성은 이미지를 보여줄 수 없을 때 해당 이미지를 대체할 텍스트를 명시합니다.


            """
            haya_item_html = driver.page_source
            haya_item_soup = BeautifulSoup(haya_item_html, "html.parser")
# //*[@id="mount_0_0_Zl"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/div[1]/img
            haya_1pic = haya_item_soup.find('img', class_='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')
            haya_1pic_url = haya_item_soup.find('img', class_='x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')
            haya_upload_id = haya_item_soup.find('div', class_='xt0psk2')
            haya_upload_location = haya_item_soup.find('a', class_= 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aaqk _a6hd')

            haya_upload_txt = haya_item_soup.find('h1', class_= "_aacl _aaco _aacu _aacx _aad7 _aade")
            haya_hash_tags = haya_item_soup.find('a', class_= "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd")
            haya_likes = haya_item_soup.find('div', class_= "x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj")
            haya_upload_date= haya_item_soup.find('time', class_= "_aaqe")

            haya_next_curser = haya_item_soup.find('div', class_= " _9zm2")
            # //*[@id="mount_0_0_Zl"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/button/div
            """

            """
            insta_utils.driver().find_element_by_css_selector("div.v1Nh3.kIKUG._bz0w").click()
            time.sleep(3)

            # 사진 저장 시작
            img_cnt = 0
            while True:
                try:
                    # 현재 게시물에서 사진 추출
                    soup = BeautifulSoup(insta_utils.driver().page_source, "html.parser")
                    img_url = soup.select_one(".FFVAD")["src"]
                    img_name = 'keyword' + "_" + str(img_cnt + 1) + ".jpg"

                    # 사진 다운로드
                    with open(img_name, "wb") as f:
                        f.write(insta_utils.driver().get(img_url).content)
                    print("다운로드 완료:", img_name)

                    # 10장 이상이면 종료
                    img_cnt += 1
                    if img_cnt >= 10:
                        break

                    # 다음 사진으로 이동
                        try:
                            metadata.HAYA9_NEXT_CURSER
                            i_button.click()
                            if metadata.HAYA9_NEXT_CURSER is None:
                                break
                """

"""
    for i, item in enumerate(items):
        new_item = read_item(item)
        i_xpath = f'//*[@id="mount_0_0_fC"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[{1}]/div[{i+1}]'

        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    print("[{}] [{}] [{}]".format(i, j, k))
"""

"""
    for article in articles:
        # 게시물 정보 출력
        print(article.select_one('a')['href'])
        print(article.select_one('img')['src'])
        print(article.select_one('img')['alt'])

    # 웹 드라이버 종료
    driver.quit()
"""


