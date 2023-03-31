# -*- coding:utf-8 -*-

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import re
import json
import pandas as pd


def extract_insta_data(
        user_id="snobx0x", user_passwd="qwer12134", wish_num=3,
        keyword="팬케이크",
        instagram_id_name="username", instagram_pw_name="password",
        instagram_login_btn=".sqdOP.L3NKy.y3zKF     ",
        first_img_css="div._ac7v._aang > div._aabd._aa8k._aanf",
        location_object_css="div._aaqm > div._aacl._aacn._aacu._aacy._aada._aade > a",
        upload_id_object_css="div._ab8w._ab94._ab97._ab9f._ab9k._ab9p._abcm > div._aacl._aaco._aacw._aacx._aad6._aade > span._aap6._aap7._aap8",
        date_object_css="div._aacl._aacm._aacu._aacy._aad6 > time._aaqe",
        main_text_object_css="div._a9zr > div._a9zs > span._aacl._aaco._aacu._aacx._aad7._aade",
        tag_css="a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._aa9_._a6hd",
        comment_more_btn="div._ab8w._ab94._ab99._ab9f._ab9k._ab9p._abcm > button._acan._acao._acas",
        comment_ids_objects_css="span._aap6._aap7._aap8 > a.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._acan._acao._acat._acaw._a6hd",
        comment_texts_objects_css="div._a9zs > span._aacl._aaco._aacu._aacx._aad7._aade",
        print_flag=True,
        next_arrow_btn_css1="div._aank > div._aaqg._aaqh > button._abl-",
        save_file_name="instagram_extract",
        save_file_name_tag="instagram_tag"
):
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    driver = wd.Chrome(ChromeDriverManager().install(), options=chrome_options)

    print(f"login start - option {login_option}")

    login_url = "https://www.instagram.com/accounts/login/"
    driver.get(login_url)
    time.sleep(10)

    is_login_success = False

    try:
        instagram_id_form = driver.find_element_by_name(instagram_id_name)
        instagram_id_form.send_keys(user_id)
        time.sleep(5)

        instagram_pw_form = driver.find_element_by_name(instagram_pw_name)
        instagram_pw_form.send_keys(user_passwd)
        time.sleep(7)

        login_ok_button = driver.find_element_by_css_selector(instagram_login_btn)
        login_ok_button.click()
        is_login_success = True
    except:
        print("instagram login fail")
        is_login_success = False

    time.sleep(10)

    if is_login_success:
        print(f"login {login_option} success")
        print(f"Start {keyword} Extract")

        url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

        instagram_tags = []
        instagram_tag_dates = []

        driver.get(url)
        time.sleep(10)

        print("login success")

        # 첫번째 게시물
        driver.find_element_by_css_selector(first_img_css).click()

        print("click first image")

        # data lists
        location_infos = []
        location_hrefs = []

        upload_ids = []

        date_texts = []
        date_times = []
        date_titles = []

        main_texts = []

        instagram_tags = []

        comments = []

        check_arrow = True

        count_extract = 0

        while True:
            print(f"count_extract - {count_extract} / wish_num - {wish_num}")
            if count_extract > wish_num:
                driver.close()
                driver.quit()
                break
            time.sleep(5.0)
            # 위치정보

            if check_arrow == False:
                break

            try:
                location_object = driver.find_element_by_css_selector(location_object_css)
                location_info = location_object.text
                print(f"location_object - {location_object}")
                print(location_object.text)
                location_href = location_object.get_attribute("href")
            except:
                location_info = None
                location_href = None

            print("get location info")
            # 올린사람 ID
            try:
                upload_id_object = driver.find_element_by_css_selector(upload_id_object_css)
                upload_id = upload_id_object.text
            except:
                upload_id = None
            print("get upload_id info")

            # 날짜
            try:
                date_object = driver.find_element_by_css_selector(date_object_css)
                date_text = date_object.text
                date_time = date_object.get_attribute("datetime")
                date_title = date_object.get_attribute("title")
            except:
                date_text = None
                date_time = None
                date_title = None

            print("get date info")

            # 본문
            try:
                main_text_object = driver.find_element_by_css_selector(main_text_object_css)
                main_text = main_text_object.text
            except:
                main_text = None

            print("main text info")

            ## 본문 속 태그
            try:
                tag_list = driver.find_elements_by_css_selector(tag_css)  # C7I1f X7jCj

                for tag in tag_list:
                    tag_raw = tag.text
                    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
                    extract_tag = ''.join(tags).replace("#", " ")  # "#" 제거

                    instagram_tags.append(extract_tag)
            except:
                pass
            print("tag info")

            # 댓글
            ## 더보기 버튼 클릭
            try:
                more_btn_list = driver.find_elements_by_css_selector(comment_more_btn)

                for more_btn in more_btn_list:
                    if '답글 보기' in more_btn.text:
                        more_btn.click()
                        time.sleep(1)
            except:
                print("----------------------fail to click more btn----------------------------------")
                pass

            print("comment info")

            ## 댓글 데이터
            try:
                comment_data = {}
                comment_ids_objects = driver.find_elements_by_css_selector(comment_ids_objects_css)
                comment_texts_objects = driver.find_elements_by_css_selector(comment_texts_objects_css)

                try:
                    for i in range(len(comment_ids_objects)):
                        comment_data[str((i + 1))] = {"comment_id": comment_ids_objects[i].text,
                                                      "comment_text": comment_texts_objects[i].text}
                except:
                    pass



            except Exception as E:
                print(E)
                comment_id = None
                comment_text = None
                comment_data = {}

            try:
                if comment_data != {}:
                    keys = list(comment_data.keys())

                    for key in keys:
                        if comment_data[key]['comment_id'] == upload_id:
                            tags = re.findall('#[A-Za-z0-9가-힣]+', comment_data[key]['comment_text'])
                            tag = ''.join(tags).replace("#", " ")  # "#" 제거

                            tag_data = tag.split()

                            for tag_one in tag_data:
                                instagram_tags.append(tag_one)
            except:
                pass

            location_infos.append(location_info)
            location_hrefs.append(location_href)

            upload_ids.append(upload_id)

            date_texts.append(date_text)
            date_times.append(date_time)
            date_titles.append(date_title)

            main_texts.append(main_text)

            comment_json = json.dumps(comment_data, ensure_ascii=False)

            comments.append(comment_json)

            if print_flag:
                print("location_info : ", location_info)
                print("location_href : ", location_href)
                print("upload id : ", upload_id)
                print("date : {} {} {}".format(date_text, date_time, date_title))
                print("main : ", main_text)
                print("comment : ", comment_data)

                print("insta tags : ", instagram_tags)

            try:
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_arrow_btn_css1)))
                time.sleep(5.0)
                next_arrow_btn = driver.find_element_by_css_selector(next_arrow_btn_css1)
                next_arrow_btn.send_keys(Keys.ENTER)

                print("click next arrow button")
            except:
                check_arrow = False

            count_extract += 1

        try:
            print("svae_data")
            insta_info_df = pd.DataFrame(
                {"location_info": location_infos, "location_href": location_hrefs, "upload_id": upload_ids,
                 "date_text": date_texts, "date_time": date_times, "date_title": date_titles, "main_text": main_texts,
                 "comment": comments})
            insta_info_df.to_csv("{}.csv".format(save_file_name), index=False)
        except:
            print("fail to save data")

        try:
            print("save_data")
            insta_tag_df = pd.DataFrame({"tag": instagram_tags})
            insta_tag_df.to_csv("{}.csv".format(save_file_name_tag), index=False)
        except:
            print("fail to save tag data")
    elif not is_login_success:
        print(f"login fail")