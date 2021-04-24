import sys

input = sys.stdin.readline

def queen(i, j):
    global cnt

    if i == N-1:
        cnt += 1
        return

    i += 1
    for k in range(N):
        if col[k] == 0 and right[N-1-i+k] == 0 and left[i+k] == 0:
            col[k] = 1
            right[N-1-i+k] = 1
            left[i+k] = 1
            queen(i, k)
            col[k] = 0
            right[N-1-i+k] = 0
            left[i+k] = 0


N = int(input())

arr = [[0]*N for _ in range(N)]

cnt = 0
col = [0] * N
right = [0] * (N*2-1)
left = [0] * (N*2-1)

for j in range(N):
    col[j] = 1
    right[N-1+j] = 1
    left[j] = 1
    queen(0, j)
    col[j] = 0
    right[N-1+j] = 0
    left[j] = 0

print(cnt)