import sys

K, N = map(int, sys.stdin.readline().split())
wires = list(map(int, [sys.stdin.readline() for _ in range(K)]))

# 이진탐색으로 N개 이상의 랜선이 나오는 길이 중 가장 긴 길이를 찾는다.
l = 1
r = max(wires)
while l <= r:
    mid = (l + r) // 2

    cnt = sum(wire // mid for wire in wires)

    if cnt >= N:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)