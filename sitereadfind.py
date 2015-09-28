# this is to read the first page html on a webpage and spot certain words in it
#-------------------------------------------------------------------------------
import re 
import urllib
from urllib.request import urlopen

k = 0

url=input("enter the url: ")
Resp = urlopen("http://www."+ url)
sitetext = Resp.read().decode("utf-8")
#print(sitetext)
Search = input('What do you want to look for in the website '+ url+ ' ?:')
found = re.findall(Search,sitetext,re.IGNORECASE)
links = re.findall('"((http|ftp)s?://.*?)"', sitetext)

# if found is not :
for find in found:
 	k = k+1
 	# print("/"+ find)
print("Total number of occurrences of ",Search,"is", k)
print("all the links are as follows:", links)