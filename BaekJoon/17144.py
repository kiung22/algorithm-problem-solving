import sys

input = sys.stdin.readline


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

total_dust = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            top = i-1
            bottom = i
        elif arr[i][j] > 0:
            total_dust += arr[i][j]

removed_dust = 0
for _ in range(T):
    stack = []
    for i in range(R):
        for j in range(C):
            diffused_dust = arr[i][j] // 5
            if diffused_dust > 0:
                for di, dj in d:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        arr[i][j] -= diffused_dust
                        stack.append((ni, nj, diffused_dust))

    while stack:
        i, j, dust = stack.pop()
        arr[i][j] += dust
    
    removed_dust += arr[top-1][0] + arr[bottom+1][0]

    for i in range(top-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    for i in range(C-1):
        arr[0][i] = arr[0][i+1]
    for i in range(top):
        arr[i][C-1] = arr[i+1][C-1]
    for i in range(C-1, 1, -1):
        arr[top][i] = arr[top][i-1]
    arr[top][1] = 0

    for i in range(bottom+1, R-1):
        arr[i][0] = arr[i+1][0]
    for i in range(C-1):
        arr[R-1][i] = arr[R-1][i+1]
    for i in range(R-1, bottom, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for i in range(C-1, 1, -1):
        arr[bottom][i] = arr[bottom][i-1]
    arr[bottom][1] = 0

print(total_dust - removed_dust)