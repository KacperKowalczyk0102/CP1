def appear(aray1,aray2):
    appears1=True
    for x in aray1:
        appears2=False
        for y in aray2:
            if x==y:
                appears2=True
                break
        if appears2==False:
            appears1=False
            break
    return appears1

aray1=[1,2,3]
aray2=[1,2,3,4,5,6]
print(appear(aray1,aray2))