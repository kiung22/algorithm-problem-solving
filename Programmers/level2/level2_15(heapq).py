# 더 맵게
import heapq as hp
def solution(scoville, K):
    count = 0
    hp.heapify(scoville)

    while len(scoville) > 1:
        first = hp.heappop(scoville)
        if first >= K:
            break
        second = hp.heappop(scoville)
        hp.heappush(scoville, first + second*2)
        count += 1

    return scoville[0] >= K and count or -1
