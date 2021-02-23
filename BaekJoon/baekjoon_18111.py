N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

count = [0] * 257
for row in blocks:
    for block in row:
        count[block] += 1

