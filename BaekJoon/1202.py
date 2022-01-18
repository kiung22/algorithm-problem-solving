import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
for _ in range(N):
    w, v = map(int, input().split())
    jewel.append((w, v))
bag = []
for _ in range(K):
    c = int(input())
    bag.append(c)

jewel.sort()
bag.sort()

heap = []
answer = 0
k = 0
for i in range(K):
    for j in range(k, N):
        if jewel[j][0] <= bag[i]:
            heapq.heappush(heap, -jewel[j][1])
            k = j + 1
        else:
            break
    if heap:
        answer += -heapq.heappop(heap)

print(answer)
