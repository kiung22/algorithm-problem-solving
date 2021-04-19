import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    max_value = 0
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i] and dp[j] > max_value:
            max_value = dp[j]
    dp[i] += max_value

print(max(dp))
