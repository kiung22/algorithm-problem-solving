import sys

input = sys.stdin.readline 

def f(i, n, k):
    if n == k:
        print(*p)
        return
    if i == N:
        return
    
    p[n] = numbers[i]
    f(i, n+1, k)
    f(i+1, n, k)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
p = [0] * M

f(0, 0, M)
