from random import randint

throw = randint(1, 6)

our_number = int(input('Podaj liczbę od 1 do 6: '))

if throw == our_number:
    print("True")
else:
    print("False")
    