for liczba in range(1,31):
    if liczba%3==0 and liczba%5 == 0:
        print('BINGO')
    elif liczba%5==0:
        print('FIVE')
    elif liczba%3==0:
        print('THREE')
    else:
        print(liczba)
    