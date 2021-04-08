import sys

input = sys.stdin.readline 

def solve(n, i, j):
    global cnt_1, cnt0, cnt1

    for r in range(i, n+i):
        for c in range(j, n+j):
            if arr[r][c] != arr[i][j]:
                for di in range(0, n, n//3):
                    for dj in range(0, n, n//3):
                        solve(n//3, i+di, j+dj)
                return

    if arr[i][j] == -1:
        cnt_1 += 1
    elif arr[i][j] == 0:
        cnt0 += 1
    else:
        cnt1 += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt_1 = 0
cnt0 = 0
cnt1 = 0
solve(N, 0, 0)

print(cnt_1)
print(cnt0)
print(cnt1)