aray=[2,3,2,5,8,1,9,8]

for x in range(0,len(aray)):
    appear=False
    for y in range(0,len(aray)):
        if aray[x]==aray[y] and x!=y:
            appear=True
    if appear==False:
        print(aray[x])