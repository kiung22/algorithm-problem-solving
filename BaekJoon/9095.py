import sys

input = sys.stdin.readline 

def solve(n):
    dp = [1, 2, 4]

    for i in range(4, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    return dp[n]


T = int(input())
for _ in range(T):
    N = int(input())

    print(solve(N))