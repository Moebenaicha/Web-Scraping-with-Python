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
            
#testlink = "https://casablanca.shopdutyfree.com/en/jack-daniels-old-no-7-5cl"



for link in productlinks:
    
    urll = requests.get(link, headers=headers)
    soup = BeautifulSoup(urll.content, 'lxml')
    name_NO = soup.find('h1', class_="page-title")
    price = soup.find('span', class_="price-container") 
    try:
        promo = soup.find('div', class_="promo-description")
    except:
        promo = 'no promo'
    whisky = {
         'name': name_NO,
         'price': price,
         'promo' : promo,                
         }
    print(whisky)
  
 
        
        
        
        
  

