# 대문자로 해놓는건 안바뀌는 것
from selenium.webdriver.common.by import By


import yeoncrawl.insta

EXTRACT_NUM = 30
# DRIVER_PATH
# "패션", "뷰티", "여행", "음식", "운동", "댄스", "피트니스", "요가", "헬스", "스킨케어", "메이크업", "헤어스타일", "스트릿패션",
#                  "유튜버", "아이돌", "먹방", "일상", "꽃", "동물", "쇼핑", "연예인", "커플룩", "애완동물", "디저트", "카페", "영화", "책",
#                  "자기계발", "음악"
HASH_TAG = "글램핑"
HASH_TAG_LIST = ["푸딩카페", "메론빵", "다꾸", "춘식이", "시티팝", "문구", "서일페", "성수동맛집", "서울수목원", "화담숲", "캠핑", "불멍",
                 "양모펠트", "불꽃놀이", "냥스타그램", "꽃놀이", "팬케이크", "포인트오브뷰", "플라워클래스", "작약", "꽃시장", "애완동물", "커피", "맥북파우치",
                 "개발자", "코딩"]
# 로그인 URL
LOGIN_URL = "https://www.instagram.com/accounts/login/"
CONTENT_URL = "https://www.instagram.com/explore/tags/"

# 로그인 ID, PW
INSTAGRAM_ID = "dhkim860715"
INSTAGRAM_PW = "dlruddus717"





# 제일 처음에 뜨는 이미지 URL.
STD_IMG_URL = 'x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3'




HASH_TAG_CSS = ""
DATE_CSS =""
MAIN_TEXT_CSS = ""




SAVE_FILE_NAME="instagram_extract"
SAVE_FILE_NAME_TAG="instagram_tag"
