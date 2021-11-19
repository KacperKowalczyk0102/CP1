file = open("numbers.txt","r")
sum = 0
for num in file:
    sum += int(num)
file.close()

print(sum)