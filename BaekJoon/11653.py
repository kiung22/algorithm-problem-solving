N = int(input())

n = 2
while N > 1:
    if N % n:
        n += 1
    else:
        print(n)
        N //= n
