import sys

input = sys.stdin.readline 

def perm(n, k):
    if n == k:
        print(*p)
        return
    for i in range(N):
        if used[i]: continue
        used[i] = 1
        p[n] = numbers[i]
        perm(n+1, k)
        used[i] = 0
        
    

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
used = [0] * N
p = [0] * M

perm(0, M)