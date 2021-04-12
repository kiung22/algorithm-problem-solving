import sys

sys.stdin = open('input.txt')

def startpoint():
    for i in range(N):
        for j in range(M-1, 54, -1):
            if arr[i][j] == '1':
                return i, j-55

def solution():
    i, j = startpoint()
    for k in range(8):
        s = arr[i][j+k*7:j+k*7+7]



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    solution()

    #print(f'#{tc} {}')

