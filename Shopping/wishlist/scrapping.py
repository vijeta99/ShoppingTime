import requests
from bs4 import BeautifulSoup
import lxml
source='https://www.amazon.in/gp/product/B08LSXRSJS/ref=ox_sc_act_title_1?smid=A2MTKUD8205HGB&psc=1'
def get_data(source):
  print('entered')

  try:
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Accept-Language":"en",}
        print('start scrapping')
        r=requests.get(source,headers=headers)
        soup=BeautifulSoup(r.text,'lxml')
        name=soup.select_one(selector="#productTitle").getText()
        name=name.strip()
       
        price=soup.select_one(selector="#priceblock_ourprice").getText()
        price=price[2:]
        price=float(price)
        print(price)
        return name, price
        #article=soup.find('article')
        #headline=article.a.text
       # for item in soup.find_all('span'):
         #   print(item.find('div',id=).text)
       # print(name)
       
            
      
       
       
  except Exception as e:
        print('Scrapping failed')
        print(e)

get_data(source)    