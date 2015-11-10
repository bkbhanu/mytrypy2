import requests
from bs4 import BeautifulSoup

CurFrom = input("What is the currency you want to convert from: ")
CurTo = input("What is the currency you want to convert To: ")
Amt = input("How many " + CurFrom + " do you want to convert: ")
url = "http://www.x-rates.com/calculator/?from=" + CurFrom + "&to=" + CurTo + "&amount=" + Amt
#print(url)

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.content,"html.parser")
nicesoup = soup.prettify()
#print(nicesoup)
links = soup.find_all("a")
k = 0
for links in soup.find_all("div"):
	if links.get("newcont") != None:
		print(links.get("newcont"))
	k = k+1
print("the total number of links is: "+ str(k))

#data = soup.find_all("span", {"class": "ccOutputRslt"}) #, {"class": "rateDown"})
data = soup.find_all("span", {"class": "ccOutputTrail"}) #, {"class": "rateDown"})
n = 0
for item in data:
	print("==================")
	print(item.text)
	print("==================")
	n = n+1
print("the number of items: ",+ n)
	