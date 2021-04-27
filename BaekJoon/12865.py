import sys

input = sys.stdin.readline

N, K = map(int, input().split())
objects = [[0, 0]]
for _ in range(N):
    objects.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = objects[i]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])