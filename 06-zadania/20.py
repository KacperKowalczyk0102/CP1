def occurs(number,array):
    appear=False
    for x in range(0,len(array)):
        
        if array[x]==number:
            appear=True
    return appear

aray2=15,38,7,23,14
print(occurs(23,aray2))