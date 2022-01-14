import sys

input = sys.stdin.readline


N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))
total_cost = sum(cost)

dp = [[0] * (total_cost+1) for _ in range(N+1)]
result = 10000
for i in range(1, N+1):
    for j in range(total_cost+1):
        if cost[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte[i-1] + dp[i-1][j-cost[i-1]], dp[i-1][j])
        
        if dp[i][j] >= M:
            result = min(result, j)

print(result)