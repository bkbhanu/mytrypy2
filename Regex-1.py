import re
print("hello world")
S=input('Whats your name:')
print("Great ! I got this working",S)
M = ("Great ! I got this working " + S)
Parse = re.split('\W',M)
print(Parse)
#S = "This is a sample text 123easy"
#Parse = re.split('\d',S)
#print(Parse)