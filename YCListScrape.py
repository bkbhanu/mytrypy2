import requests
from bs4 import BeautifulSoup

url = "http://ycuniverse.com/ycw15"
#print(url)

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.content,"html.parser")
nicesoup = soup.prettify()
#print(nicesoup)
#links = soup.find_all("a")
#k = 0
#for links in soup.find_all("div"):
#	if links.get("newcont") != None:
#		print(links.get("newcont"))
#	k = k+1
#print("the total number of links is: "+ str(k))

Body = soup.find_all("tbody") #, {"style": "margin-bottom: 9px;"}) #, {"class": "rateDown"})
print(Body.contents)
##n = 0
#for Comp in Body:
#	href = Comp.get("href")
#	print(href)
#	n = n + 1
#	print("total =" + str(n))
##
#print(Comp)

#n = 0
#for item in Body:
#	print("==================")
#	print(item.text)
#	print("==================")
#	n = n+1
#print("the number of items: ",+ n)
	