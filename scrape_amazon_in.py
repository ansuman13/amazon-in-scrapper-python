from pprint import pprint
from bs4 import BeautifulSoup
import requests

userinput = input("search for a book :")
userinput.replace(" ","+")
url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords="+str(userinput)
# url = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords=to+kill+a+mocking+bird&rh=n%3A976389031%2Ck%3Ato+kill+a+mocking+bird'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

soup = BeautifulSoup(response.content,'lxml')
# print(soup.prettify())
linkdp  = soup.find("a",{ "class" : "a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"})
print(linkdp)

div=soup.find("div",{"class":"a-row a-spacing-none"})
dp = div.a['href']
dp1 = dp.split('/')
userdp = dp1[5]


from pprint import pprint
from bs4 import BeautifulSoup
import requests

url = 'http://www.amazon.in/dp/'+ userdp
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

soup = BeautifulSoup(response.content,"lxml")
print(soup.prettify())
title = soup.find(id="productTitle")
if title != None:
	print(title.text)
image = soup.find(id="imgBlkFront")
print(image["data-a-dynamic-image"][2:92])
price = soup.find("span",{"class":"a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"})
if price == None:
	price = soup.find("span",{"class":"a-color-price"})
lprice = price.text
print(lprice)
# print(lprice[3:])
papertype = soup.find("span",{"class":"a-size-medium a-color-secondary a-text-normal"})
print(papertype.text)
author = soup.find("a",{"class":"a-link-normal contributorNameID"})
if author == None:
	author = soup.find("a",{"class":"a-link-normal"})
print(author.text)
print(url)