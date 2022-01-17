# import sys
# import heapq

# input = sys.stdin.readline

# N, K = map(int, input().split())
# jewel = []
# for _ in range(N):
#     w, v = map(int, input().split())
#     jewel.append((w, v))
# bag = []
# for _ in range(K):
#     c = int(input())
#     bag.append(c)

# jewel.sort(key=lambda x: (x[0], x[1]))
# bag.sort()

# heap = []
# i = 0
# j = 0
# count = K
# flag = False
# while i < N and j < K:
#     if jewel[i][0] > bag[j]:
#         j += 1
#         if flag == False and len(heap) < j:
#             count -= 1
#         flag = False
#     else:
#         if len(heap) == count:
#             heapq.heappushpop(heap, jewel[i][1])
#         else:
#             heapq.heappush(heap, jewel[i][1])
#         i += 1
#         flag = True

# print(sum(heap))


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

jewel.sort(key=lambda x: (x[0], x[1]))
bag.sort()

jewel_list = [[] for _ in range(K)]
i = 0
j = 0
while i < N and j < K:
    if jewel[i][0] <= bag[j]:
        jewel_list[j].append(jewel[i])
        i += 1
    else:
        j += 1

heap = []
count = 0
for i in range(K-1, -1, -1):
    k = len(jewel_list[i])
    count += 1
    for j in range(k-1, -1, -1):
        if len(heap) < count:
            heapq.heappush(heap, jewel_list[i][j][1])
        else:
            heapq.heappushpop(heap, jewel_list[i][j][1])

print(sum(heap))