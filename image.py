import requests
import random

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
    while item["CategoryCode"] != "ART" or item["AccessLevel"] != "Unrestricted" or item["FilePath"] == "notavailable.png": #product achieved is classified under Art and has an image
        item = get_item()
    return item #returns a dict of the product details