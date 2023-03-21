from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
from django.http import HttpResponse

def read_item(item):
    return item
def crawldaangn(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://www.daangn.com/region/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C/%EC%84%B1%EB%8F%99%EA%B5%AC')
    time.sleep(3)
    itemhtml = driver.page_source
    itemsoup = BeautifulSoup(itemhtml, "html.parser")
    items = itemsoup.select('article.card-top')
    result = []
    for i, item in enumerate(items):
        new_item = read_item(item)
        a_xpath = f'//*[@id="content"]/section[1]/article[{i+1}]/a'
        a_button = driver.find_element(By.XPATH, a_xpath)
        a_button.click()
        a_item_html = driver.page_source
        new_item.category = a_item_html.find('')
        driver.back()
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn.btn-more-blue')
    print("crawlstart")
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