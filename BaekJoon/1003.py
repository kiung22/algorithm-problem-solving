import sys

def f(n):
    if len(fibo) > n:
        return fibo[n]
    
    f1 = f(n-1)
    f2 = f(n-2)
    fibo.append([f1[0]+f2[0], f1[1]+f2[1]])
    return fibo[n]

T = int(input())

fibo = [[1, 0], [0, 1]]

for _ in range(T):
    n = int(sys.stdin.readline())

    f(n)

    print(*fibo[n])
