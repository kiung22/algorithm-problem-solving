import sys

input = sys.stdin.readline 

def solution():
    q = []
    zero = True
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    q.append((i, j, k))
                elif arr[i][j][k] == 0:
                    zero = False
    if zero:
        return 0

    # bfs
    day = 0
    while q:
        day += 1
        q_tmp = []
        while q:
            i, j, k = q.pop()
            for di, dj, dk in d:
                ni = i+di
                nj = j+dj
                nk = k+dk
                if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and arr[ni][nj][nk] == 0:
                    arr[ni][nj][nk] = day
                    q_tmp.append((ni, nj, nk))
        q = q_tmp
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return -1
    return day-1


# 입력
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 6방향
d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

print(solution())
