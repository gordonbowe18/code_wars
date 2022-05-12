#Write a function that receives two strings and returns n, where n is equal to the number of characters we should shift the first string forward to match the second. The check should be case sensitive.

#For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been rotated 5 characters forward to produce the second string, so 5 would be returned.
#If the second string isn't a valid rotation of the first string, the method returns -1. 

def shifted_diff(first, second):
    n = 0
    if len(first) != len(second) or sorted(first) != sorted(second): 
        n = -1
        return n
    else:
        while first != second and n < len(first):
            first = first[-1] + first 
            first = first[:-1]
            print (first)
            n = n + 1
    if n == len(first):
        n = -1
    return n