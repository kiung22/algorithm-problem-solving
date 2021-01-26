def checkio(number):
    n = 1
    for m in str(number):
        if int(m):
            n *= int(m)
    return n
