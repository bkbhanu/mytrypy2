import os
import sys
from urllib.request import urlopen
from urllib.error import *

#url="http://www."+ input("Enter the URL you need the Title for: ")
url="http://www"
#tagtype=input("What Tag do you want to search for:")
#tagS= "<"+tagtype
#tagF= "</"+tagtype
#btagS=tagS.encode('utf-8')
#btagF=tagF.encode('utf-8')
try:
    Resp = urlopen(url)    
#except URLError as E:
#    Resp2 = E.reason
#    Resp3 = E.args
#    Resp4 = E.strerror
#    #Resp2 = E.reason
#    Resp3 = str(E)
#    Resp5 = str(Resp3)
#    #Resp3 = Resp2[2]
#    #Resp2 = E.strerror
#    #Resp3 = Resp2.find('11004')
#    #.encode('utf-8')
#    import re
#    if re.search("11004", Resp5):
#        print('gotcha', Resp5, Resp3, E)
except URLError as E:
    if E.reason.errno == 11004:
        Resp2 = E.reason.errno
        print('test done', Resp2)
    #Resp2=E
#except urllib.error.URLError.errno as E:
    #Resp2=E
#if URLError.errno == 11004
#print("gotthis")
#except urllib.error.URLError.reason as R
#except Exception urllib.error.URLError as R:
#print(R)
#except URLError.reason as R:
   
#except urllib.error.URLError.errno as E:
 #   print(E)
#except URLError as O:
 #  print(O)
#except HTTPError as B:
 #  print(B)
#except URLError.errno, A:
 #   print('you got an error with the code', A)
#print A
#print(Resp)