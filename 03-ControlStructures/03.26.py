GoodPin = 2379
Pin = 0

for możliwość in range(3):
    Pin = int(input("Podaj Pin: "))
    if Pin == GoodPin:
        print('Pin jest poprawyny')
    else:
        print("Pin jest niepoprawny...")
print('Przepraszamy, twoja karta została zablokowana.')