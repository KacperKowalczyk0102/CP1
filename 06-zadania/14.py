aray=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
longest=""
for x in range(0,len(aray)):
    if len(aray[x])>len(longest):
        longest=aray[x]
        
print(longest)