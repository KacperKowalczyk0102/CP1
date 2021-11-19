file = open('countries.txt','r')
i = 1
for line in file:
     print(f'{i} {line}')
     i+= 1
file.close()