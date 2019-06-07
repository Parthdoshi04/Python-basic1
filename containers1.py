li=['black','red','green','white','red','white','yellow','black','green']
lj=[]
print(li)
for x in li:
    if x not in lj:
        lj.append(x)
    else:
        break
print(lj)
lj.sort()
print(lj)
