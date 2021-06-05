import requests
import random
# from bs4 import BeautifulSoup
# import HTMLSession from requests_html
from requests_html import HTMLSession
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait



TOTAL_IMGS = 24062

def generate_rand_img(total):
    num = random.randint(1, total)
    return num

def get_item():
    url_search = "https://collections.nationalgallery.sg/PublicApi/ProductApi/getproduct"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    data = {"ProductId":str(generate_rand_img(TOTAL_IMGS))}
    req= requests.post(url_search, headers=headers, json=data)
    j=req.json()
    while j["Status"] != "OK":
        data = {"ProductId":str(generate_rand_img(TOTAL_IMGS))}
        req= requests.post(url_search, headers=headers, json=data)
        j=req.json()
    item_info = j["Products"][0]
    return item_info

def get_art_item():
    item = get_item()
    while item["CategoryCode"] != "ART" or item["AccessLevel"] != "Unrestricted" or item["FilePath"] == "notavailable.png":
        item = get_item()
    return item #returns a dict

get_art_item()


# # url = "https://collections.nationalgallery.sg/#/details/Home/" + str(generate_rand_img(TOTAL_IMGS))
# url = "https://collections.nationalgallery.sg/#/details/Home/13620"
# print(url)

# driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver = webdriver.Chrome('/chromedriver')
# driver.get(url)

# wait = WebDriverWait(driver, 2)

# # title = driver.find_element_by_class_name("col-md-12 text-center mt-3 mb-3 p-0")
# title = driver.find_element_by_xpath("//div[@class='col-md-12 text-center mt-3 mb-3 p-0']/p[@ng-bind-html='item.SourceTitle']").get_attribute("ng-binding")

# print(title)

# driver.close()