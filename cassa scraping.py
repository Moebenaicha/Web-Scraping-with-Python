from bs4 import BeautifulSoup
import requests

baseurl = 'https://casablanca.shopdutyfree.com/'

headers = {'User-Agemt': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

productlinks = []
 
for x in range(1,2):
    url = requests.get(f'{"https://casablanca.shopdutyfree.com/en/liquor/whisky?p=[x]"}')
    soup = BeautifulSoup(url.content,'lxml')
    
    productlist = soup.find_all('div', class_='product-item-info')
    
   
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
        
print(len(productlinks)) 
        
        
        
        
  

