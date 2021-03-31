# 입력
N = int(input())
data = [tuple(map(int, input().split())) for i in range(N)]

for A in data:
    rank = 1
    for B in data:
        if A[0] < B[0] and A[1] < B[1]:
            rank += 1
    print(rank, end=' ')
