def sqaure(n,a):
    return a**n
x=1
a=1
n=2
while (x<=10):
##    a = int(input("what is the number:"))
##    n = int(input("What is the exponent:"))
    print(a)
    print(n)
    outFile=open('C:\Python34\programs\writefile2.txt','a')
##    sq == square(n,a)
##    print("returning",y)
    print("The result is: ", sqaure(n,a))
    outFile.write('\nThe result is: '+ str(sqaure(n,a)))
    a=a+1
    n=n+1
    x=x+1
    outFile.close()



