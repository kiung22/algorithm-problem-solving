import sys

input = sys.stdin.readline 

def gcd(n1, n2):
    if n2 > n1:
        n1, n2 = n2, n1
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)

def f(M, N, x, y):
    if M > N:
        M, N = N, M
        x, y = y, x

    limit = lcm(M, N)
    for i in range(y, limit+1, N):
        p = i % M
        if p and x == p:
            return i
        if p == 0 and x == M:
            return i
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    print(f(M, N, x, y))
