import Sort

def minmax(array):
    Sort.bubblesort(array)
    return [array[0],array[len(array)-1]]

a=[4,2,8,4,7,9,5]
print(minmax(a))