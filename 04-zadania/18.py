def count(number):
    number = str(number)
    sum = 0
    for i in range (0,len(number)):
        sum = sum + int(number[i])
    return sum

n = int(input())
print(count(n))
        
        