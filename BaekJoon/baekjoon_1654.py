import sys

K, N = map(int, sys.stdin.readline().split())
wires = list(map(int, [sys.stdin.readline() for _ in range(K)]))
wires.sort(reverse=True)

LAN = []    # 가능한 랜선의 길이를 담은 리스트
for i in range(K):
    k = (i + 1) * K
    for j in range(1, N - k + 2):
        LAN.append(wires[i] // j)
LAN.sort() # 이진탐색을 위해 정렬
print(LAN)

# 이진탐색으로 N개 이상의 랜선이 나오는 길이 중 가장 긴 길이를 찾는다.
left = 0
right = len(LAN) - 1
while left <= right:
    middle = (left + right) // 2

print(result)