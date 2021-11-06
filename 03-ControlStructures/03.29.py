a = int(input("Wprowadź liczbę: "))

suma = 0
średnia = 0
ilość = 0

while a!= 0:
    suma = suma + a
    ilość = ilość + 1
    a = int(input("Wprowadź liczbę: "))
średnia = suma/ilość

print(f"WYNIK: Ilość={ilość}, Suma={suma}, Średnia={średnia}")