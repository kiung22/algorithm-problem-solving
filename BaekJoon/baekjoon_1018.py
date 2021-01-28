N, M = map(int, input().split())
board = [input() for i in range(N)]

result = N * M
for n in range(N - 7):
    for m in range(M - 7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[n+i][m+j] == 'WB'[(i+j)%2]:
                    cnt += 1
        cnt = min([cnt, 64-cnt])
        if result > cnt:
            result = cnt

print(result)
