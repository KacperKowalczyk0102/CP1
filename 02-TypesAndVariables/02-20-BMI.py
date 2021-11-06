weight = int(input("Podaj swoją wagę w kg: "))

height = int(input("Podaj swój wzrost w cm: "))

BMI = round(weight/ (height**2) * 10000, 1)

print(f'BMI: {BMI}')
