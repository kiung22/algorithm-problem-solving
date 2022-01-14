import sys

input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+2-i):
        if numbers[j] == numbers[j+i-1]:
            if i <= 2:
                dp[j][j+i-1] = 1
            else:
                dp[j][j+i-1] = dp[j+1][j+i-2]

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(dp[i][j])