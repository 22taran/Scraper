from selectorlib import Extractor
import requests
import json

ext = Extractor.from_yaml_file('css_format.yml')

def scrape(url):  

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    return ext.extract(r.text)
print("What are you are looking for!!!!")
item=input()
a = "https://www.amazon.com/s?k=" +item    
data=scrape(a)
if data:
    for product in data['products']:
    	product['search_url'] = a
    	print("Product: %s"%product['title'])
    	print(json.dumps(product, indent=4))