import os
from urllib.request import urlopen
from urllib.error import *

Num = input("How many sites do you want to lookup")
#isinstance(Num,int)
See = isinstance(Num,int)
#N = 1
#if Num != int(Num):
#    N=0
#else:
#    N=1
#while Num != int(Num):
while See == False:
#if isinstance(Num,int) == False:
    print('Try again')
    Num = input("How many sites do you want to lookup")
    if Num != int(Num):
        See == False
    else:
        See == True
        #if See == True:
    #    N=1
print('you are out of the loop')           
#url="http://www."+ input("Enter the URL you need the Title for: ")
#tagtype=input("What Tag do you want to search for:")
#tagS= "<"+tagtype
#tagF= "</"+tagtype
#btagS=tagS.encode('utf-8')
#btagF=tagF.encode('utf-8')
#Resp = urlopen(url)
#Page=Resp.read()
#GetLinkS=Page.find(btagS)
#print(GetLinkS)
#GetLinkF=Page.find(btagF)
#print(GetLinkF)
#GetTitle = Page[(GetLinkS+7):GetLinkF]
#print(GetTitle)
