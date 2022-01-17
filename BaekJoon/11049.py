import sys

input = sys.stdin.readline

N = int(input())
shape = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(N - i):
        dp[j][j+i] = 2 ** 31
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + shape[j][0] * shape[k][1] * shape[j+i][1])

print(dp[0][N-1])