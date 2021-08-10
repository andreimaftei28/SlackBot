import re
import json
import time
from bs4 import BeautifulSoup as bs
from scrapping_tool.selenium_driver import driver

def get_katas(url):
    """
    :param url: link to scrape 
    :return: a json file with a list of exercises to be posted on slack
    """
    try:
        driver.implicitly_wait(20)
        driver.get(url)
        for _ in range(10):
            # scroll down the page in order to scrape more exercises
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        soup = bs(driver.page_source, "lxml")
        driver.close()
        print("Driver closed!")
        katas = []
        regex_title = re.compile('^list-item')
        regex_difficulty = re.compile('^item-title')

        kata_title = soup.find_all("div", attrs={"class": regex_title})
        kata_diff = soup.find_all("div", attrs={"class": regex_difficulty})

        zipped_katas = list(zip(kata_diff, kata_title))
        for i, x in enumerate(zipped_katas):
            difficulty = x[0]
            title = x[1]

            katas.append({
                "id": f"id-{i}",
                "diff": difficulty.get_text()[:5],
                "title": f"{title.get('data-title')}",
                "kata_link": f'https://www.codewars.com/kata/{title.get("id")}/train/python'
            })

        with open("katas.json", 'w') as json_file:
            json.dump(katas, json_file)

    except Exception as e:
        print(e, '>>>>>>>>>>>>>>>Exception>>>>>>>>>>>>>>',sep="\n")

