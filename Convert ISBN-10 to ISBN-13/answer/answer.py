def isbn_converter(isbn):
    isbn = isbn[:-1]
    isbn = "978-" + isbn
    temp = isbn.replace('-','')
    b = [int(a) for a in str(temp)]
    for i in range(0, len(b)):
        if i % 2 == 0:
            b[i] = b[i]
        else:
            b[i] = (b[i] * 3)
    x = sum(b)
    w = x % 10
    check = 0
    if w != 0:
        check = 10 - w
    isbn = isbn + str(check)
    return isbn