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
print(url)
result=soup.find('li',id='result_0')
print(result.prettify())