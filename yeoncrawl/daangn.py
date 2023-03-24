from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time
from django.http import HttpResponse

def read_item(item):
    return item
def crawldaangn(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # 당근에 '성동구'를 검색하면 뜨는 정보를 selenium 으로 모사하기 위해서 driver.get  방식으로 불러온다
    driver.get('https://www.daangn.com/region/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C/%EC%84%B1%EB%8F%99%EA%B5%AC')
    # 너무많은 요청을 한번에 불러오면 내 url을 차단 할 수 있어서, 3초간 슬립을 걸어준다.
    time.sleep(3)
    item_html = driver.page_source
    item_soup = BeautifulSoup(item_html, "html.parser")
    # BeautifulSoup로 html을 다 불러온다.
    items = item_soup.select('article.card-top')
    # 'article.card-top'라는 형식으로 당근 마켓의 아이템들은 구성되어있다.
    results = []
    # 내가 넣은 아이템의 각각 값을 딕셔너리로 넣을 result 를 for문 외부에 넣는다.
    # 크롬 우클릭 -> 검사-> 크롤링 할 해당 아이템 찾기-> copy ->copy XPath ..
    # XPath를 어디 VSC, Sublime text 같은데 적어둔다.
    for i, item in enumerate(items): # i는 0 부터 시작한다. items 개별 항목들 각각의 item에 숫자를 각각 붙여준다.
        new_item = read_item(item)
        a_xpath = f'//*[@id="content"]/section[1]/article[{i+1}]/a' # 이게 아까 복사한 XPath , 규칙성이 보인다.
        a_button = driver.find_element(By.XPATH, a_xpath) # selenium으로 클릭을 모사해야 하니, driver로 불러준다.
        a_button.click() #클릭모사
        time.sleep(2) # 로딩을 하는  시간을 줘야 읽는다 적어도 2초 이상은 줘야 한다.
        a_item_html = driver.page_source # 클릭을 한번 해서 뜬 곳
        a_item_soup = BeautifulSoup(a_item_html, "html.parser")
        # BeautifulSoup로 a_item_html 을 다 불러온다.
        new_item_name = a_item_soup.find('h1', id='article-title')  # 아이템의 이름
        new_item_category = a_item_soup.find('p', id="article-category") #아이템의 카테고리
        item_data = {
            'new_item_name': new_item_name.text.strip(), # bs 고유의 메소드
            'new_item_category': new_item_category.text.strip()
        }
        print(item_data)
        time.sleep(1)
        results.append(item_data)
        driver.back() # 뒤로가기 클릭 모사
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn.btn-more-blue')
    print("crawlstart")
    print(results)
    return HttpResponse("crawlDone")

#             if 'clickLink' in car:
#                 linksources = car['clickLink']
#                 for linksource in linksources:
#                     linknum = linksource.split()
#                     linkxpath = f'//*[@id="estimationModel"]/div[2]/div[1]/section/ul/li[{linknum[0]}]/div[{linknum[1]}]/label[{linknum[2]}]/span'
#                     linkbutton = driver.find_element(By.XPATH, linkxpath)
#                     driver.execute_script(f"window.scrollTo(0,0)")
#                     linkbutton.click()
#                     time.sleep(3)
#                     trimhtml = driver.page_source
#                     trim_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn.btn-more-blue')
#                     trimsoup = BeautifulSoup(trimhtml, "html.parser")
#                     temp_trims = trimsoup.select('article.list-article')
#                     if temp_trims:
#                         for trim, button in zip(temp_trims, trim_buttons):
#                             temp_trim = maketrims(trim, driver, button)
#                             print(temp_trim['trim_name'])
#                             result_trims['trims'].append(temp_trim)
#         results.append(result_trims)
#     temp_crawldata.jsondata = results
#     temp_crawldata.save()
#
#
# def maketrims(trim, driver, button):
#     trim_name = trim.find('h4')
#     trim_price = trim.find('span', class_="price")
#     trim_images = trim.findAll('img')
#     action = ActionChains(driver)
#     result_trim = {'trim_name': trim_name.text, 'trim_price': trim_price.text.replace("\n", "")}
#     for i, image in enumerate(trim_images):
#         imgname = f'img{i}'
#         imgsrc = f'imgsrc{i}'
#         result_trim[imgname] = image['alt']
#         result_trim[imgsrc] = f'https://www.hyundai.com{image["src"]}'
#     result_trim['option'] = []
#     action.move_to_element(button).perform()
#     button.click()
#     time.sleep(3)
#     # driver.switch_to_window(driver.window_handles[1])
#     option_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.list-title')
#     for option_button in option_buttons:
#         option_button.click()
#         time.sleep(1)
#     optionhtml = driver.page_source
#     optionsoup = BeautifulSoup(optionhtml, "html.parser")
#     options = optionsoup.select('div.list-item.active')
#     for option in options:
#         temp_option = {"label": option.find('div', class_="title").text.strip()}
#         plist = option.findAll('p', class_="dot")
#         for i, p in enumerate(plist):
#             temp_option[i] = p.text.strip()
#         result_trim['option'].append(temp_option)
#     close_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/button')
#     close_button.click()
#     time.sleep(3)
#     return result_trim