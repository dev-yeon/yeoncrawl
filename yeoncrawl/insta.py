from elasticsearch import Elasticsearch, helpers
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from django.http import HttpResponse
import yeoncrawl.metadata as data
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from django.http import JsonResponse
from selenium.webdriver import ActionChains
import os
from .models import Post, PostImg
from .serializers import PostSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

port = 9200
elasticsearch_hosts = [
    'https://search-yeon-emiary-ljdngztcn7zfrs5tot3rzzpkki.ap-northeast-2.es.amazonaws.com',
]
elasticsearch_id = 'yeon'
elasticsearch_password = 'Yeon123!'
auth = (elasticsearch_id, elasticsearch_password)
keyword = openapi.Parameter('keyword', openapi.IN_QUERY, description="키워드", type=openapi.TYPE_STRING)


def gen_post(index):
    posts = Post.objects.all()
    for post in posts:
        serializers = PostSerializer(post)
        result = serializers.data
        result.update({"_index": index})
        result.update({"_id": post.id})
        yield result


def bulk_direct_post(request):
    es = Elasticsearch(hosts=elasticsearch_hosts, post=port, http_auth=auth, timeout=30)
    response = helpers.bulk(es, gen_post("insta_post"))
    return HttpResponse(f'bulk to es Done with {response}')


@swagger_auto_schema(
    method='post',
    operation_id='키워드 검색',
    operation_description='키워드로 검색 후 해당 결과 반환합니다.',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'keyword': openapi.Schema(type=openapi.TYPE_STRING, description="검색어"),
        }
    ),
    tags=['검색'],
    responses={200: openapi.Response(
        description="200 OK",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'result': openapi.Schema(type=openapi.TYPE_OBJECT, description="Search result"),
            }
        )
    )}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def search(request):
    search_word = request.data['keyword']
    es = Elasticsearch(hosts=elasticsearch_hosts, post=port, http_auth=auth)
    index = "insta_post"
    body = {
        'size': 1000,
        'query': {
            'match': {
                "post_tag": search_word
            }
        }
    }
    res = es.search(index=index, body=body)
    return JsonResponse(res)

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
    hashtag_list = data.HASH_TAG_LIST
    for hashtag in hashtag_list:
        driver.get(f"{data.CONTENT_URL}{hashtag}/")
        time.sleep(11)
        # 게시물 가져오기
        divs = driver.find_elements(By.TAG_NAME, "div")
        idstring=""
        for div in divs:
            idstring =div.get_attribute("id")
            if idstring.startswith("mount"):
                break
        print(idstring)
        #게시물 가져오기
        driver.execute_script("window.scrollTo(0, 300)")
        duplicate_list = []
        for j in range(1, 4):
            for k in range(1, 4):
                i_path = f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[{j}]/div[{k}]'
                i_button = driver.find_element(By.XPATH, i_path)
                action = ActionChains(driver)
                action.move_to_element(i_button).perform()
                i_button.click()
                time.sleep(3)
                """
                temp_post = Post()
                data.STD_IMG_URL 
                temp_postimg = PostImg()   # 새로운 이미지 저장할 그릇 생성
                temp_post.save()  # 한번 세이브 해서 일단 Post db에 새로운 데이터 생성
                temp_postimg.save()
                """

                # 클릭을 한번 해서 뜬 곳
                item_soup = BeautifulSoup(driver.page_source, "html.parser")
                # BeautifulSoup로  클릭 해서 뜬 곳 html
                temp_post = Post(post_tag=hashtag)
                h1names = item_soup.select("h1", class_="_aacl._aaco._aacu._aacx._aad7._aade")
                temp_desc = ""
                for h1name in h1names:
                    temp_desc += h1name.text.strip()
                temp_post.post_desc = temp_desc
                creatordivs = item_soup.select("div", class_="_a9zr")
                for creatordiv in creatordivs:
                    divnames = creatordiv.select("h2", class_="_a9zc")
                    for i, divname in enumerate(divnames):
                        creatorname = divname.text.strip()
                        if creatorname is not None and creatorname != "":
                            if not creatorname.__contains__("인기"):
                                if not creatorname.__contains__("최근"):
                                    temp_post.author_id = creatorname
                likesections = item_soup.select("section", class_="_ae5m._ae5n._ae5o")
                likestr = ""
                for likesection in likesections:
                    likestrings = likesection.select("span",
                                                     class_="x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")
                    for likestring in likestrings:
                        likestr = likestring.text.strip()
                temp_post.like_string = likestr
                temp_post.save()
                postimglist = item_soup.select("ul", class_="_acay")
                for postimg in postimglist:
                    # if postimg:
                        img_list = postimg.findAll('img')
                        for img in img_list:
                            temp_postimg = PostImg()
                            temp_postimg.img_url = img["src"]
                            temp_postimg.img_alt = img["alt"]
                            temp_postimg.img_tag = hashtag
                            if not temp_postimg.img_alt.__contains__("프로필"):
                                if not temp_postimg.img_alt in duplicate_list:
                                    temp_postimg.save()
                                    duplicate_list.append(img["alt"])
                                    temp_post.img_list.add(temp_postimg)
                                    temp_post.save()
                driver.back()
                time.sleep(1)
                # 인기 게시글을 보기위한  스크롤 내리기 구현

        # for l in range(1, 9):
        #     for m in range(1, 4):
        #                 #f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]/'
        #         i_path = f'//*[@id="{idstring}"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{l}]/div[{m}]'
        #         i_button = driver.find_element(By.XPATH, i_path)
        #         i_button.click()
        #         time.sleep(3)
        #         item_soup = BeautifulSoup(driver.page_source, "html.parser")
        #
        #         postimglist = item_soup.select("ul", class_="_acay")
        #         for postimg in postimglist:
        #                     # if postimg:
        #             img_list = postimg.findAll('img')
        #             for img in img_list:
        #                 temp_postimg = PostImg()
        #                 temp_postimg.img_url = img["src"]
        #                 temp_postimg.img_alt = img["alt"]
        #                 temp_postimg.img_tag = data.HASH_TAG
        #                 if not temp_postimg.img_alt.__contains__("프로필"):
        #                     temp_postimg.save()
        #         driver.back()
        #
        #     driver.execute_script("window.scrollTo(0, 700)")

    return HttpResponse("Done Crawl")
