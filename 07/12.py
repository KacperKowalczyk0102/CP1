file = open('shopping.txt','a')
product= input('Enter the product: ')
file.write(product + '\n')

file.close()