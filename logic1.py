count=0
a=int(input("enter value for a"))
b=int(input("enter value for b"))
c=int(input("enter value for c"))
for x in range(a,b):
    if((x%c==0)):
        count=count+1
        print(x)
    else:
        count=count
print("Total Count",count)
