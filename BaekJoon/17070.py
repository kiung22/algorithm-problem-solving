import sys

input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[[0]*3 for _ in range(N)] for _ in range(N)]

visited[0][1][0] = 1
for j in range(2, N):
    if arr[0][j]:
        break
    visited[0][j][0] = 1

for i in range(1, N):
    for j in range(1, N):
        if arr[i][j] == 0:
            visited[i][j][0] += visited[i][j-1][0] + visited[i][j-1][2]
            visited[i][j][1] += visited[i-1][j][1] + visited[i-1][j][2]

            if arr[i][j-1] == 0 and arr[i-1][j] == 0:
                visited[i][j][2] += sum(visited[i-1][j-1])

print(sum(visited[N-1][N-1]))