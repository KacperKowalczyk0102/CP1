import mymath

myNumber = mymath.read_numbers()
randomNumber = mymath.generate_number()

if myNumber == randomNumber:
    print("Great!")
else:
    print("Not this time")