import sys

input = sys.stdin.readline

def find_set(n):
    while n != p[n]:
        n = p[n]
    return n

def union_set(x, y):
    if x != y:
        if truths[y]:
            p[x] = y
        else:
            p[y] = x

def solution():
    for party in parties:
        if party[0] > 1:
            x = find_set(party[1])
            for i in range(2, len(party)):
                y = find_set(party[i])
                union_set(x, y)
    
    ans = M
    for party in parties:
        for i in range(1, len(party)):
            n = party[i]
            x = find_set(n)
            if truths[x]:
                ans -= 1
                break
    return ans


N, M = map(int, input().split())
truths = [0] * (N+1)
for i in list(map(int, input().split()))[1:]:
    truths[i] = 1
parties = [list(map(int, input().split())) for _ in range(M)]

p = [i for i in range(N+1)]

print(solution())