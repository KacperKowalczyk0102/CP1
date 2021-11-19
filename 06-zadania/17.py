
aray=[4,36,12,28,9,44,5]
aray=[5,1,36]

for x in aray:
    number=False
    for y in aray2:
        if x==y:
            number=True
    if number==False:
        print(x)