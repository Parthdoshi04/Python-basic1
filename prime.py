n=int(input("enter a number"))
for x in range(2,n):
    if((n%x==0)):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("not prime")
else:
    print("it is prime")
