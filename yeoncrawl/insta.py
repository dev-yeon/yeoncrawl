
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import yeoncrawl.insta_utils
import yeoncrawl.metadata as metadata
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from .models import Post, PostImg

def instagram_login():
    chrome_options = Options()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    # 인스타그램 접속
    driver.get(metadata.LOGIN_URL)
    time.sleep(2)
    # 로그인
    username = 'snobx0x'
    time.sleep(1)
    password = 'qwer12134'
    time.sleep(1)
    login = driver.find_element(By.NAME, "username")
    login.send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    time.sleep(3)

    return driver

# 인스타의 html 코드를 insta_soup 에 넣기
def insta_soup(request):
    driver = instagram_login()
    # 해시태그 검색
    driver.get(f"{metadata.CONTENT_URL}{metadata.HASH_TAG}/")
    print("hashtag")
    time.sleep(30)
    # 게시물 가져오기
    divs = driver.find_elements(By.TAG_NAME, "div")
    idstring=""
    for div in divs:
        idstring =div.get_attribute("id")
        if idstring.startswith("mount"):
            break
    print(idstring)
    #게시물 가져오기

    for j in range(1, 4):
        for k in range(1, 4):
            i_path = f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[{j}]/div[{k}]'
                   # f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]'
            i_button = driver.find_element(By.XPATH, i_path)
            i_button.click()
            time.sleep(3)
            temp_post = Post()
            temp_post.save()  # 한번 세이브해서 일단 Post db에 새로운 데이터 생성
            # 클릭을 한번 해서 뜬 곳
            # temp_postimg = PostImg()  # 새로운 이미지 저장할 그릇 생성

            item_soup = BeautifulSoup(driver.page_source, "html.parser")
            # BeautifulSoup로  클릭해서 뜬
            temp_url = item_soup.find('', class_="")  # url 주소
            print(temp_url)
            std_img_url = item_soup.find('div', class_="_aagv") # 처음 뜬 img url 주소
            print(std_img_url)
            author_id = item_soup.find('div', class_="xt0psk2")   # 작성자 id
            print(author_id)
            post_desc = item_soup.find('div',class_="_a9zs") # 글 설명 내용
            print(post_desc)
            location = item_soup.find('div', class_="_aacl _aacn _aacu _aacy _aada _aade")  # 글 올린 곳 주소
            print(location)
            like_count = item_soup.find('a',class_="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj") # 게시글 좋아요 갯수
            print(like_count)
            post_date = item_soup.find('a', class_="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd") # 게시글 날짜
            print(post_date)
            # img_list = item_soup.find('', id='') # img list url
            # print(img_list)
            # time.sleep(2)
            # temp_postimg.save()
            # temp_post.img_list.add(temp_postimg)
            # temp_post.save()
            # std_img_url=
            # author_id=//*[@id="{idstring}"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/div/div/a
            #
            # Post(models.Model):
            #std_img_url=
            #post_desc=

            # location=
            #like_count=
            #post_date=
            #img_list=
            # //*[@id="mount_0_0_sl"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/div/div/a
            #뒤로가기
            driver.back()
            # img_url
            # img_alt
            # img_name
            # 인기 게시글을 보기위한  스크롤 내리기 구현

    driver.execute_script("window.scrollTo(0, 700)")
    time.sleep(3)



    for l in range(1, 9):
        for m in range(1, 4):
                    #f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]/'
            i_path = f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]'
            i_button = driver.find_element(By.XPATH, i_path)
            i_button.click()
            time.sleep(3)

            # 뒤로가기
            driver.back()
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(3)

        """
            temp_post = Post()  # models 의 Post 호출
            temp_post.save() #한번 세이브해서 일단 Post db에 새로운 데이터 생성
            #  ------------------------
            temp_postimg = PostImg()  # 새로운 이미지 저장할 그릇 생성
            temp_postimg.img_url = ['srcset', 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']
            temp_postimg.save()
            temp_post.img_list.add(temp_postimg)
            temp_post.save()
            """
    return item_soup

# 인기게시물 9개 읽기 (하드코딩)
def hayatteru_9(request):
    driver = yeoncrawl.insta_utils.driver(request)

    for j in range(1, 4):
        for k in range(1, 4):
            i_path = f'//*[@id="mount_0_0_fC"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[{j}]/div[{k}]'
            i_button = driver.find_element(By.XPATH, i_path)
            i_button.click()
            time.sleep(3)
            temp_post = Post()  # models 의 Post 호출
            temp_post.save() #한번 세이브해서 일단 Post db에 새로운 데이터 생성
            #  ------------------------
            temp_postimg = PostImg()  # 새로운 이미지 저장할 그릇 생성
            temp_postimg.img_url = ['srcset', 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3']
            temp_postimg.save()
            temp_post.img_list.add(temp_postimg)
            temp_post.save()
            count = 0
