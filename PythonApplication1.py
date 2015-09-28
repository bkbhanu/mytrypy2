## --- internet access

import os
import urllib
#from urllib.request import urlopen

url="http://www."+ input("Enter the URL you need the Title for: ")
tagtype=input("What Tag do you want to search for:")
tagS= "<"+tagtype
tagF= "</"+tagtype
btagS=tagS.encode('utf-8')
btagF=tagF.encode('utf-8')
Resp = urlopen(url)
Page=Resp.read()
GetLinkS=Page.find(btagS)
print(GetLinkS)
GetLinkF=Page.find(btagF)
print(GetLinkF)
GetTitle = Page[(GetLinkS+7):GetLinkF]
print(GetTitle)
##for line in Page:
##    if '<title>' in line:
##        print(line)
##Many=Resp.read().count('<title>')
##print(Many)
##Page=Page.split('\n')
##first3=Page[0:3]
##print(Page)
##print(first3)
