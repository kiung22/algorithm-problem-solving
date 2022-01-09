import sys

input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

def solve(n):
    INF = 100000000
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][n] = RGB[0][n]
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i][j] = min(RGB[i][j] + dp[i-1][k], dp[i][j])
    dp[-1][n] = INF
    return min(dp[-1])

print(min(solve(0), solve(1), solve(2)))