n= int(input("enter a number"))
s=0
while(n!=0) :
    r=n%10
    s=s*10 + r
    n=n//10
print("the reversed number is " + str(s))
