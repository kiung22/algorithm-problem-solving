# 입력
N, M = map(int, input().split())
board = [input() for i in range(N)]

# min_cnt: 최소 횟수
min_cnt = N * M
# (n, m)을 시작점으로 하는 8 x 8 배열의 색칠해야 하는 횟수 확인
for n in range(N - 7):
    for m in range(M - 7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[n+i][m+j] == 'WB'[(i+j)%2]:
                    cnt += 1
        # cnt: B부터 시작할 때 색칠해야하는 횟수
        # 64 - cnt: W부터 시작할 때 색칠해야하는 횟수
        cnt = min([cnt, 64-cnt])
        if min_cnt > cnt:
            min_cnt = cnt

print(min_cnt)
