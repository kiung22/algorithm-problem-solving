def checkio(data):
    upper = []
    lower = []
    digit = []
    for d in data:
        if d.isupper():
            upper.append(d)
        elif d.islower():
            lower.append(d)
        elif d.isdigit():
            digit.append(d)
        else:
            pass
    if len(data) >= 10 and upper and lower and digit:
        return True
    else:
        return False
