# this is to read a file and spot certain words in it
#--------------------------------------------------------
import re 
import urllib

outfile=open('/Users/Bhanu/Code/Py/Seekh/Filereadtest.txt','rt')
text=outfile.read()
#textmine = re.compile(r'\bClients\b')
k = 0
#for line in text
#	matched_text = textmine.findall()
Search = input('What do you want to look for in the file: ')
found = re.findall(Search,text,re.IGNORECASE)
#print(found)
#if found is not :
for find in found:
	k = k+1
	print("/"+ find)
print("Total number of occurrences of ",Search,"is", k)
outfile.close()