import sys

input = sys.stdin.readline


def remove_star(n, r, c):
    for i in range(n):
        for j in range((n-i)*2-1):
            arr[r+n+i][c+(i+1)*2-1+j] = ' '

def f(n, r, c):
    if n == 1:
        return 
    
    n //= 2
    remove_star(n, r, c)

    f(n, r, c)
    f(n, r+n, c)
    f(n, r+n, c+n*2)


N = int(input())
arr = [['*'] * (i*2+1) for i in range(N)]

f(N, 0, 0)

for row in arr:
    print(''.join(row).center(N*2-1, ' '))
