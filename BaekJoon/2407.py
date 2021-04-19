import sys

input = sys.stdin.readline 

n, r = map(int, input().split())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] * i

# nCr = n! / (n-r)!r!
print(dp[n] // (dp[n-r] * dp[r]))