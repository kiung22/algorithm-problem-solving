import sys

input = sys.stdin.readline

def queen(i):
    global cnt

    if i == N:
        cnt += 1
        return

    for j in range(N):
        if col[j] == 0 and right[N-1-i+j] == 0 and left[i+j] == 0:
            col[j] = 1
            right[N-1-i+j] = 1
            left[i+j] = 1
            queen(i+1)
            col[j] = 0
            right[N-1-i+j] = 0
            left[i+j] = 0


N = int(input())

arr = [[0]*N for _ in range(N)]

cnt = 0
col = [0] * N
right = [0] * (N+N-1)
left = [0] * (N+N-1)

queen(0)

print(cnt)