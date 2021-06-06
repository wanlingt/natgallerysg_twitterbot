import tweepy
import requests
import os
from image import get_art_item
from local_settings import *


def twitter_api():
    # Send our keys and tokens to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api
    # try:
    #     api.verify_credentials()
    #     print("Authentication OK")
    # except:
    #     print("Error during authentication")

def item_info():
    """
    Retrieves the relevant artwork details (Title, Artist, Date, Prod ID, URL, image URL)
    Returns the details as a dictionary
    """
    img_details = get_art_item()
    title = img_details["SourceTitle"]
    artist = img_details["Artist"]
    date = img_details["ProductDate"]
    prod_id = img_details["ProductId"]
    url = f'https://collections.nationalgallery.sg/#/details/Home/{prod_id}'
    details_str = f'{artist}, {title}. {date}. {url}'
    img_url = f'https://production-ngssource.s3-ap-southeast-1.amazonaws.com/asset/Artwork/{img_details["FilePath"]}'
    item_info = {"message": details_str, 
                "img_url": img_url}
    return item_info

def tweet_image(url, message):
    """
    Updates twitter status with an image from a given url and a message string
    """
    api = twitter_api()
    filename = '/tmp/temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

if __name__ == "__main__":
    item = item_info()
    tweet_image(item["img_url"], item["message"])


