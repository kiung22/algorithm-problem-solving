import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# padding
arr = [[0] * (N+1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

# 누적합
for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] += arr[i][j-1]
for i in range(1, N+1):
    for j in range(1, N+1):
        arr[j][i] += arr[j-1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(ans)