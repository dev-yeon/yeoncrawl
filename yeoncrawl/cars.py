
def crawltrim_s3(request):
    crawls = CrawlData.objects.filter(title__contains="basiccar")
    cars = crawls[0].jsondata
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    results = []
    temp_crawldata = CrawlData()
    temp_crawldata.title = str(datetime.datetime.now().date()) + "cartrim"

    for car in cars:
        result_trims = {'car_name': car['car_name'], 'trims': [], 'brand': car['brand']}
        if car['brand'] == "hyundai" and 'makingLink' in car:
            driver.get(car['makingLink'])
            time.sleep(3)
            carhtml = driver.page_source
            carsoup = BeautifulSoup(carhtml, "html.parser")
            trims = carsoup.select('article.list-article')
            buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn.btn-more-blue')
            if trims:
                for trim, button in zip(trims, buttons):
                    temp_trim = maketrims(trim, driver, button)
                    print(temp_trim['trim_name'])
                    result_trims['trims'].append(temp_trim)
            if 'clickLink' in car:
                linksources = car['clickLink']
                for linksource in linksources:
                    linknum = linksource.split()
                    linkxpath = f'//*[@id="estimationModel"]/div[2]/div[1]/section/ul/li[{linknum[0]}]/div[{linknum[1]}]/label[{linknum[2]}]/span'
                    linkbutton = driver.find_element(By.XPATH, linkxpath)
                    driver.execute_script(f"window.scrollTo(0,0)")
                    linkbutton.click()
                    time.sleep(3)
                    trimhtml = driver.page_source
                    trim_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.btn.btn-more-blue')
                    trimsoup = BeautifulSoup(trimhtml, "html.parser")
                    temp_trims = trimsoup.select('article.list-article')
                    if temp_trims:
                        for trim, button in zip(temp_trims, trim_buttons):
                            temp_trim = maketrims(trim, driver, button)
                            print(temp_trim['trim_name'])
                            result_trims['trims'].append(temp_trim)
        results.append(result_trims)
    temp_crawldata.jsondata = results
    temp_crawldata.save()


def maketrims(trim, driver, button):
    trim_name = trim.find('h4')
    trim_price = trim.find('span', class_="price")
    trim_images = trim.findAll('img')
    action = ActionChains(driver)
    result_trim = {'trim_name': trim_name.text, 'trim_price': trim_price.text.replace("\n", "")}
    for i, image in enumerate(trim_images):
        imgname = f'img{i}'
        imgsrc = f'imgsrc{i}'
        result_trim[imgname] = image['alt']
        result_trim[imgsrc] = f'https://www.hyundai.com{image["src"]}'
    result_trim['option'] = []
    action.move_to_element(button).perform()
    button.click()
    time.sleep(3)
    # driver.switch_to_window(driver.window_handles[1])
    option_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.list-title')
    for option_button in option_buttons:
        option_button.click()
        time.sleep(1)
    optionhtml = driver.page_source
    optionsoup = BeautifulSoup(optionhtml, "html.parser")
    options = optionsoup.select('div.list-item.active')
    for option in options:
        temp_option = {"label": option.find('div', class_="title").text.strip()}
        plist = option.findAll('p', class_="dot")
        for i, p in enumerate(plist):
            temp_option[i] = p.text.strip()
        result_trim['option'].append(temp_option)
    close_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/button')
    close_button.click()
    time.sleep(3)
    return result_trim