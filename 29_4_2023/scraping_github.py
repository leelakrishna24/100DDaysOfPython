import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/leelakrishna24"
req = requests.get(github_profile)
scraper = bs(req.content,"html.parser")
profile_picture = scraper.find("img", {"alt":"Avatar"})["src"]

for item in scraper.find_all('img'):
    print(item['src'])

import cv2
path = profile_picture