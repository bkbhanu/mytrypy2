import requests
import ssl
from bs4 import BeautifulSoup

CurFrom = input("What is the FROM Airport: ")
CurTo = input("What is the TO Airport: ")
#Amt = input("How many " + CurFrom + " do you want to convert: ")
url = "http://www.world-airport-codes.com/distance/?a1=" + CurFrom + "&a2=" + CurTo
print(url)

r = requests.get(url, verify=False)
#print(r.text)

#data = soup.find_all("span", {"class": "ccOutputRslt"}) #, {"class": "rateDown"})
data = soup.find_all("div", {"class": "box-pad"}) #, {"class": "rateDown"})
n = 0
for item in data:
	print("==================")
	print(item.text)
	print("==================")
	n = n+1
print("the number of items: ",+ n)
	