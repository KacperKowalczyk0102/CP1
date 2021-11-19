aray=[15, 8, 31, 47, 2, 19]
for x in range(0,int(len(aray)/2)):
    variable=aray[len(aray)-x-1]
    
    aray[len(aray)-x-1]=aray[x]
    aray[x]=variable
print(aray)