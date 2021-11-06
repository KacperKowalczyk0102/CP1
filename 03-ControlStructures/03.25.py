poziom = int(input())
pion = int(input())
print('*'*poziom)
for i in range(pion-2):
    print('*' + ' '*(poziom-2)+'*')
print('*'*poziom)