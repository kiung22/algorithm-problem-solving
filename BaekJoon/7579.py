import sys

input = sys.stdin.readline

def f(i, m, c):
    global min_cost

    if m >= M:
        min_cost = min(min_cost, c)
        return
    
    if c >= min_cost:
        return
    
    for j in range(i+1, N):
        if m + byte_sum[j] < M:
            return
        f(j, m + byte[j], c + cost[j])


N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))
byte_sum = byte[:] + [0]
for i in range(N, 0, -1):
    byte_sum[i-1] += byte_sum[i]

min_cost = 10000
f(-1, 0, 0)

print(min_cost)
print(byte_sum)