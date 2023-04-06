# 대문자로 해놓는건 안바뀌는 것
from selenium.webdriver.common.by import By


import yeoncrawl.insta

EXTRACT_NUM = 30
# DRIVER_PATH

HASH_TAG = "글램핑"
HASH_TAG_LIST = ["패션", "뷰티", "여행", "음식", "운동", "댄스", "피트니스", "요가", "헬스", "스킨케어", "메이크업", "헤어스타일", "스트릿패션",
                 "유튜버", "아이돌", "먹방", "일상", "인테리어", "꽃", "동물", "쇼핑", "연예인", "커플룩", "애완동물", "디저트", "카페",
                 "영화", "책", "자기계발", "음악"]
# 로그인 URL
LOGIN_URL = "https://www.instagram.com/accounts/login/"
CONTENT_URL = "https://www.instagram.com/explore/tags/"

# 로그인 ID, PW
INSTAGRAM_ID = "snobx0x"
INSTAGRAM_PW = "qwer12134"





# 제일 처음에 뜨는 이미지 URL.
STD_IMG_URL = 'x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3'
"""
# 게시글의 설명.
POST_DESC = "h1._aacl._aaco._aacu._aacx._aad7._aade"
# 게시글 작성자.
AUTHOR_ID = "div.xt0psk2"
# 게시글을 작성자가 올린 주소.
LOCATION = "div._aacl._aacn._aacu._aacy._aada._aade"
# 좋아요 갯수.
LIKE_COUNT ="span.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"
# 글 올린 날짜.
POST_DATE = f"#{idstring} > div > div > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > div._ae5u._ae5v._ae5w > div > div > a > div > time"
# 연속된 이미지 URLs.
IMG_LIST = f"#{idstring} > div > div > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6 > div > article > div > div._ae65 > div > div > div._ae2s._ae3v._ae3w > div._ae5u._ae5v._ae5w > div > div > a > div > time"
# 최대 10 장 저장이 가능 하다.

# 다음 사진을 갈 수 있는 화살표.
NEXT_ARROW_BTN= f"#{idstring} > div > div > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x47corl.xh8yej3.x15h9jz8.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.xir0mxb.x1juhsu6 > div > article > div > div._aatk._aatl > div > div._aamn > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x10l6tqk.x1ey2m1c.x13vifvy.x17qophe.xds687c.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > button > div"
"""



HASH_TAG_CSS = ""
DATE_CSS =""
MAIN_TEXT_CSS = ""




SAVE_FILE_NAME="instagram_extract"
SAVE_FILE_NAME_TAG="instagram_tag"

# INSTAGRMA_LOGIN_BTN = ".sqdOP.L3NKy.y3zKF     "
# FACEBOOK_LOGIN_PAGE_BTN_CSS_1 = ".sqdOP.L3NKy.y3zKF     "
# FACEBOOK_LOGIN_PAGE_BTN_CSS_2 = ".sqdOP.yWX7d.y3zKF     "
# FACEBOOK_ID_FORM_NAME = "email"
# FACEBOOK_PW_FORM_NAME = "pass"
# FACEBOOK_LOGIN_BTN = "login"
# FIRST_IMG_CSS = "div._ac7v._aang > div._aabd._aa8k._aanf"



# LOCATION_CSS = "div._aaqm > div._aacl._aacn._aacu._aacy._aada._aade > a"
# UPLOAD_USER_ID_CSS = "div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._abcm > div._aacl._aaco._aacw._aacx._aad6._aade > span._aap6._aap7._aap8"
# DATE_CSS = "div._aacl._aacm._aacu._aacy._aad6 > time._aaqe"
# MAIN_TEXT_CSS = "div._a9zr > div._a9zs > span._aacl._aaco._aacu._aacx._aad7._aade"
# HASH_TAG_CSS = "a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._aa9_._a6hd"
# COMMENT_MORE_BTN = "div.qF0y9.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm                                                                                                               > button.sqdOP.yWX7d.y3zKF     "
# COMMENT_ID_CSS = "span._aap6._aap7._aap8 > a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._acan._acao._acat._acaw._a6hd"
# COMMENT_TEXT_CSS="div._a9zs > span._aacl._aaco._aacu._aacx._aad7._aade"
# PRINT_FLAG = False
# NEXT_ARROW_BTN_CSS_1="div._aank > div._aaqg._aaqh > button._abl-"
# SAVE_FILE_NAME="instagram_extract"
# SAVE_FILE_NAME_TAG="instagram_tag"