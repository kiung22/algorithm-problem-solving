import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

i = N-1
ans = 0
while K:
    coin = coins[i]
    if K >= coin:
        ans += K // coin
        K %= coin
    i -= 1

print(ans)