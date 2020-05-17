import requests
import json
from bs4 import BeautifulSoup
url = 'https://scrapethissite.com/pages/forms/'
team_name = input("Enter team name: ")
per_page = input("Enter per-page: ")
data = requests.get(url,params = {'q': team_name, 'per_page': per_page}).text
soup = BeautifulSoup(data,'html.parser')
tags = soup.find_all('tr',{'class':'team'})
lis = list()
for det in tags:
	dict = {}
	dict['team_name'] =det.find('td',{'class':'name'}).text.strip()
	dict['year'] =det.find('td',{'class':'year'}).text.strip()
	dict['wins'] =det.find('td',{'class':'wins'}).text.strip()
	lis.append(dict)
jstr = json.dumps(lis,indent = 2)
print(jstr)	
	 