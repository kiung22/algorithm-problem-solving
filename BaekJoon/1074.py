import sys

input = sys.stdin.readline 

def z(n, r, c):
    ans = 0

    while n > 0:
        x = 2 ** (n-1)
        if c >= x:
            ans += x ** 2
            c -= x
        if r >= x:
            ans += x ** 2 * 2
            r -= x
        n -= 1
    
    return ans
    

N, r, c = map(int, input().split())

print(z(N, r, c))
