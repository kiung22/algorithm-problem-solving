import heapq


def solution(jobs):
    N = len(jobs)

    heap = []
    for i, job in enumerate(jobs):
        heapq.heappush(heap, (job[0] + job[1], job[0], job[1], i))

    i = -1
    t = 0
    total = 0
    while heap:
        print(heap)
        end, start, time, j = heapq.heappop(heap)
        dt = t - start if t > start else 0

        if i == j:
            total += time + dt
            print(total)
            t = end
        else:
            i = j
            end = start + time + dt
            heapq.heappush(heap, (end, start, time, i))

    return total

print(solution([[0, 3], [3, 6], [2, 6]]))