wiekL = int(input("Wprowadź wiek psa w latach ludzkich: "))

if wiekL<=2:
    wiekP = wiekL * 10.5
    print(f'Wiek w psich latach:{wiekP}')
else:
    wiekP = 21+(wiekL-2) * 4
    print(f'Wiek w psich latach:{wiekP}')
