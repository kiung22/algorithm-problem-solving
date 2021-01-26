def checkio(expression):
    brackets = ['(', ')', '{', '}', '[', ']']
    small = '()'
    mid = '{}'
    big = '[]'
    expression = list(filter(lambda x: x in brackets, list(expression)))
    brac = ''.join(expression)
    while small in brac or mid in brac or big in brac:
        if small in brac:
            a = brac.index(small)
            expression[a:a+2] = []
            brac = ''.join(expression)
        if mid in brac:
            a = brac.index(mid)
            expression[a:a+2] = []
            brac = ''.join(expression)
        if big in brac:
            a = brac.index(big)
            expression[a:a+2] = []
            brac = ''.join(expression)
    return not(expression)
