import sys

input = sys.stdin.readline

def f(x, n):
    if n == 1:
        return x
    y = f(x, n//2)
    if n%2:
        return y * y * x % X
    else:
        return y * y % X

ans = 0
X = 1000000007
M = int(input())
for _ in range(M):
    N, S = map(int, input().split())

    N_inverse = f(N, X-2)
    Q = S * N_inverse % X
    ans += Q
    ans %= X

print(ans)