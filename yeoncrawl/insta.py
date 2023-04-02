import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import yeoncrawl.insta_utils
import yeoncrawl.metadata as metadata
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from .models import Post, PostImg

def maketrims(trim, driver,button):
    trim_img_url = trim.find('div', class_="x9f619.x1n2onr6.x1ja2u2z")
    trim_author_id = trim.find('div', class_="xt0psk2")
    trim_post_desc = trim.find('h1', class_="_aacl._aaco._aacu._aacx._aad7._aade")
    trim_location = trim.find('div', clsss_="_aacl._aacn._aacu._aacy._aada._aade")
    trim_like_count = trim.find('span', class_="x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")
    trim_post_date = trim.find('div', class_="_aacl._aacm._aacu._aacy._aad6")
    action = ActionChains(driver)
    result_trim = {trim_img_url : trim_img_url.text,
                  trim_author_id : trim_author_id.text,
                  trim_post_desc : trim_post_desc.text,
                  trim_location : trim_location.text,
                  trim_like_count: trim_like_count.text,
                  trim_post_date: trim_post_date.text}
    for i , image in enumerate(trim_images):
        imgname = f'img{i}'
        imgsrc = f'imgsrc{i}'
        result_trim[imgname] = image['alt']
        result_trim[imgsrc] = ""
    result_trim['option'] = []
    action.move_to_element(button).perform()
    button.click()
    time.sleep(3)

    option_buttons = driver.find_elements(By.CSS_SELECTOR, 'button~~~~')

    click_next_arrow_button()





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

def click_next_arrow_button(driver):
    try:
        WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, data.NEXT_ARROW_BTN)))
        time.sleep(5.0)
        next_arrow_btn =driver.find_element_by_css_selector(data.NEXT_ARROW_BTN)
        next_arrow_btn.send_keys(Keys.ENTER)
        check_arrow = True
    except:
        check_arrow = False
    return check_arrow

# 인스타의 html 코드를 insta_soup 에 넣기
def insta_soup(request):
    instas = crawls[0].jsondata
    driver = instagram_login()


    # 해시태그 검색
    driver.get(f"{metadata.CONTENT_URL}{metadata.HASH_TAG}/")
    print("hashtag")
    time.sleep(30)
    # 게시물 가져오기
    divs = driver.find_elements(By.TAG_NAME, "div")
    idstring = ""
    results = []
    temp_crawldata = CrawlData()
    temp_crawldata.title = str(datetime.datetime.now().date()) + "instatrim"
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

            temp_postimg = PostImg()   # 새로운 이미지 저장할 그릇 생성
            temp_post.save()  # 한번 세이브 해서 일단 Post db에 새로운 데이터 생성
            temp_postimg.save()
            result_trims = {'std_img_url': j['std_img_url'],
                            'author_id': ['author_id'],
                            'post_desc': ['post_desc'],
                            'location': ['location'],
                            'like_count': ['like_count'],
                            'post_date': ['post_date']}

            # 클릭을 한번 해서 뜬 곳
            item_soup = BeautifulSoup(driver.page_source, "html.parser")
            # BeautifulSoup로  클릭 해서 뜬 곳 html
            #std_img_url = item_soup.find('div', class_="_aagv") # 처음 뜬 img url 주소
            std_img_url = driver.find_elements(By.CSS_SELECTOR, data.STD_IMG_URL)
            print(std_img_url)
            # author_id = item_soup.find('div', class_="xt0psk2")   # 작성자 id
            author_id = driver.find_elements(By.CSS_SELECTOR, data.AUTHOR_ID)
            print(author_id)
            post_desc = driver.find_elements(By.CSS_SELECTOR, data.POST_DESC)
            print(post_desc)
            location = driver.find_elements(By.CSS_SELECTOR, data.LOCATION)
            print(location)
            like_count = driver.find_elements(By.CSS_SELECTOR, data.LIKE_COUNT)
            print(like_count)
            post_date = driver.find_elements(By.CSS_SELECTOR, data.POST_DATE)
            print(post_date)
            img_list = driver.find_elements(By.CSS_SELECTOR,data.POST_DATE)
            print(img_list)
            time.sleep(2)
            temp_postimg.save()
            temp_post.img_list.add(temp_postimg)
            temp_post.save()
            driver.back()


            # 인기 게시글을 보기위한  스크롤 내리기 구현

    driver.execute_script("window.scrollTo(0, 700)")
    time.sleep(3)
    for l in range(1, 9):
        for m in range(1, 4):
            i_path = f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]'
            i_button = driver.find_element(By.XPATH, i_path)
            i_button.click()
            time.sleep(3)
            temp_post = Post()
            temp_postimg = PostImg()  # 새로운 이미지 저장할 그릇 생성
            temp_post.save()  # 한번 세이브 해서 일단 Post db에 새로운 데이터 생성
            temp_postimg.save()
            # 클릭을 한번 해서 뜬 곳
            # temp_postimg = PostImg()  # 새로운 이미지 저장할 그릇 생성
            item_soup = BeautifulSoup(driver.page_source)
            # BeautifulSoup로  클릭해서 뜬
            std_img_url = driver.find_elements(By.CSS_SELECTOR, 'data.STD_IMG_URL')
            print(std_img_url)
            # author_id = item_soup.find('div', class_="xt0psk2")   # 작성자 id
            author_id = driver.find_elements(By.CSS_SELECTOR, 'data.AUTHOR_ID')
            print(author_id)
            post_desc = driver.find_elements(By.CSS_SELECTOR, 'data.POST_DESC')
            print(post_desc)
            location = driver.find_elements(By.CSS_SELECTOR, 'data.LOCATION')
            print(location)
            like_count = driver.find_elements(By.CSS_SELECTOR, 'data.LIKE_COUNT')
            print(like_count)
            post_date = driver.find_elements(By.CSS_SELECTOR, 'data.POST_DATE')
            print(post_date)
            img_list = driver.find_elements(By.CSS_SELECTOR, 'data.POST_DATE')
            print(img_list)
            time.sleep(2)
            temp_postimg.save()
            temp_post.img_list.add(temp_postimg)
            temp_post.save()

            driver.back()
        driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(3)
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
