
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


import yeoncrawl.metadata as data
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
    driver.get(data.LOGIN_URL)
    time.sleep(2)
    # 로그인
    username = data.INSTAGRAM_ID
    time.sleep(1)
    password = data.INSTAGRAM_PW
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
    driver.get(f"{data.CONTENT_URL}{data.HASH_TAG}/")
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
            i_button = driver.find_element(By.XPATH, i_path)
            i_button.click()
            time.sleep(3)
            temp_post = Post()
            temp_postimg = PostImg()   # 새로운 이미지 저장할 그릇 생성
            temp_post.save()  # 한번 세이브 해서 일단 Post db에 새로운 데이터 생성
            temp_postimg.save()
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
                    #f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]/'
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
            item_soup = BeautifulSoup(driver.page_source, "html.parser")
            # BeautifulSoup로  클릭해서 뜬
            std_img_url = driver.find_elements(By.CSS_SELECTOR, 'img')
            print(std_img_url)

            # author_id = item_soup.find('div', class_="xt0psk2")   # 작성자 id
            author_id = driver.find_elements(By.CSS_SELECTOR, 'a')
            print(author_id)

            post_desc = driver.find_elements(By.CSS_SELECTOR, 'h1')
            print(post_desc)

            location = driver.find_elements(By.CSS_SELECTOR, 'a')
            print(location)

            like_count = driver.find_elements(By.CSS_SELECTOR, 'a.x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd')
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

