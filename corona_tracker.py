import requests
import json
from bs4 import BeautifulSoup
con = input("Enter country: ")
nurl = "https://www.worldometers.info/coronavirus/"
nd = requests.get(nurl).text
s = BeautifulSoup(nd,"html.parser")
if con.upper() == "USA" or con.upper()=="UAE" or con.upper == "UK":
    con = con.upper()
else:
    con = con.title()

tag = s.find('td',string=con)
tc = tag.find_next('td')
nc = tc.find_next('td')
td = nc.find_next('td')
nde = td.find_next('td')
tr = nde.find_next('td')
ac = tr.find_next('td')
print("total cases:",tc.string)
if nc.string!=None: print("new cases:",nc.string)
print("total deaths:",td.string)
if nde.string!=None: print("new deaths:",nde.string)
print("recoveries:",tr.string)
print("active cases:",ac.string)

