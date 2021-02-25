N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

count = [0] * 257
for row in blocks:
    for block in row:
        count[block] += 1

for i in range(257):
    if count[i]:
        L = i
        break

for i in range(256, -1, -1):
    if count[i]:
        R = i
        break

time = 0
while L < R:
    if count[L] <= B and count[L] <= count[R] * 2:
        B -= count[L]
        time += count[L]
        count[L+1] += count[L]
        count[L] = 0
        L += 1
    else:
        B += count[R]
        time += count[R] * 2
        count[R-1] += count[R]
        count[R] = 0
        R -= 1

print(time, L)