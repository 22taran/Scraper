from bs4 import BeautifulSoup
import requests
import json

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache',
    }



print("Please enter item URL")
url = input()
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, features="lxml")


#WHICH THINGS I WANT TO EXTRACT
title = soup.select("#productTitle")[0].getText().strip("\n")

stock =soup.select("#availability_feature_div")[0].getText().strip("\n")

categories = []
for li in soup.select("#wayfinding-breadcrumbs_container ul.a-unordered-list")[0].findAll("li"):
	categories.append(li.get_text().strip())

features = []
for li in soup.select("#feature-bullets ul.a-unordered-list")[0].findAll('li'):
	features.append(li.get_text().strip())

price = soup.select("#priceblock_ourprice")[0].get_text()

review_count = int(soup.select("#acrCustomerReviewText")[0].get_text().split()[0])





#OUTCOME
jsonObject = {'TITLE': title, 'STOCK': stock, 'PRICE': price,'REVIE_COUNT': review_count, 'CATEGORIES': categories, 'FEATURES': features}
print(json.dumps(jsonObject, indent=2, ensure_ascii=False))