


a = int(input('Wartość a: '))
b = int(input('Wartość b: '))
c = int(input('Wartość c: '))

#p - połowa obwodu trójkąta

p = (a + b + c) / 2

area = (p*(p-a)*(p-b)*(p-c))**0.5

print(area)
