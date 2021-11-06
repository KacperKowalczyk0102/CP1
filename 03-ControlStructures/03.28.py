składnik1 = 0
składnik2 = 1
for i in range(1,51):
    print(f"{składnik1} ",end="")
    #po dodaniu koeljny sładnik jest suma poprzednich
    pomocnicza = składnik1 + składnik2
    #przesówamy o jeden składnik
    składnik1 = składnik2
    składnik2 = pomocnicza