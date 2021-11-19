aray=[2,2,6,3,6,5,2,3]
aray2=aray
a=0
b=len(aray)-1
for x in range(0,len(aray)):
    if aray[x]%2==0:
        aray2[a]=aray[x]
        a=a+1
    else:
        aray2[b]=aray[x]
        b=b-1
print(aray2)