from pprint import pprint
from bs4 import BeautifulSoup
import requests

url = 'http://www.amazon.in/dp/0099549484'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

soup = BeautifulSoup(response.content)
# print(soup.prettify())
title = soup.find(id="productTitle")
print(title.text)
image = soup.find(id="imgBlkFront")
print(image["data-a-dynamic-image"][2:92])
price = soup.find("span",{"class":"a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"})
lprice = price.text
print(lprice[3:])
papertype = soup.find("span",{"class":"a-size-medium a-color-secondary a-text-normal"})
print(papertype.text)
author = soup.find("a",{"class":"a-link-normal contributorNameID"})
print(author.text)
