import requests
import json
from bs4 import BeautifulSoup
url = "https://scrapethissite.com/pages/simple/"
data = requests.get(url)
soup = BeautifulSoup(data.text,'html.parser')
tags = soup.find_all('div',{'class':'col-md-4 country'})
country_list = list()
for i in tags:
	dict = {}
	t1 = i.find_next('h3')
	dict['country_name'] = t1.text.strip()
	t2 = i.find_next('span',{'class':'country-capital'})
	dict['country_capital'] = t2.text.strip()
	t3 = i.find_next('span',{'class':'country-population'})
	dict['population'] = t3.text.strip()
	t4 = i.find_next('span',{'class':'country-area'})
	dict['area'] = t3.text.strip()
	country_list.append(dict)
jstr = json.dumps(country_list,indent = 2)
print(jstr)	