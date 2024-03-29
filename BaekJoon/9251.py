import sys

input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
N1 = len(S1)
N2 = len(S2)

dp = [[0] * (N2+1) for _ in range(N1+1)]
for i in range(1, N1+1):
    for j in range(1, N2+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] += dp[i-1][j-1]+1
        else:
            dp[i][j] += max(dp[i][j-1], dp[i-1][j])

print(dp[i][j])
