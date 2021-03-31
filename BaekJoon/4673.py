def d(n):
    return n + sum(map(int, list(str(n))))

selfNumbers = list(range(1, 10000))
for i in range(1, 10000):
    if d(i) in selfNumbers:
        selfNumbers.remove(d(i))
for selfNumber in selfNumbers:
    print(selfNumber)
