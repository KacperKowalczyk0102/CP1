array = [-15,8,-31,47,-2,19]

minimum = array[0]
maximum = array[0]

for number in array:
    if number > maximum:
        maximum = number
    
    if number < minimum:
        minimum = number

print(f'Minimum: {minimum}
    