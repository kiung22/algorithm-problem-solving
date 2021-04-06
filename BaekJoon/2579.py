import sys


N = int(input())
stair = [int(sys.stdin.readline()) for _ in range(N)]

if N < 3:
    print(sum(stair))
else:
    d = [0] * N
    d[0] = stair[0]
    d[1] = stair[0] + stair[1]
    d[2] = max(stair[0], stair[1]) + stair[2]

    for i in range(3, N):
        d[i] = stair[i] + max(d[i-2], d[i-3] + stair[i-1])

    print(d[-1])
