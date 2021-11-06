kwota = 18
piątki = kwota//5
kwota = kwota%5

dwójki = kwota//2
kwota = kwota%2

jedynki = kwota
print(f'5 zł - {piątki}\n2 zł - {dwójki}\n1 zł - {jedynki}')
