def page_digits(pages):
    #Sort it for those that can't go len-2
    if pages < 10: 
        x = (range(1, pages + 1))
        list_for_length = []
        for i in x: 
            i = str(i)
            list_for_length.append(len(i))
        return sum(list_for_length)
    # and everyone else!
    else: 
        y = ''
        length = len(str(pages))
        l = '9' * (length - 1)
        y = str(length - 2) + ('8' * (length-2)) + '9'
        y = int(y)
        y = y + (((pages - int(l)) * length))
        return y    


    