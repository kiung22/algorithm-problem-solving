import sys

input = sys.stdin.readline 

def z(n, r, c):
    global ans 

    if n == 0:
        return

    x = 2 ** (n-1)
    if c >= x:
        ans += x ** 2
        c -= x
    if r >= x:
        ans += x ** 2 * 2
        r -= x
    print(ans)
    z(n-1, r, c)


N, r, c = map(int, input().split())

arr = [[0]*2**N for _ in range(2**N)]

ans = 0
z(N, r, c)

print(ans)
