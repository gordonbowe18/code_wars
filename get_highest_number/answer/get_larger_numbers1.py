
def get_larger_numbers(a, b):
    x = (len(a))
    y = 0
    new_array = []
    while y < x:
        if a[y] > b[y]:
            new_array.append(a[y])
        elif a[y] < b[y]:
            new_array.append(b[y])
        else: 
            new_array.append(a[y])
        y = y + 1 
    return new_array

print (get_larger_numbers([] , []))