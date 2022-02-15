import heapq


def solution(jobs):
    jobs.sort()
    N = len(jobs)

    heap = []
    heapq.heappush(heap, (jobs[0][0] + jobs[0][1], jobs[0][0], jobs[0][0], jobs[0][1]))
    t = jobs[0][0]
    i = 1
    total_response_time = 0
    
    while heap:
        end, start, request, time = heapq.heappop(heap)

        if start < t:
            end = time + t
            start = t
            heapq.heappush(heap, (end, start, request, time))
        else:
            t = end
            total_response_time += end - request
            while i < N and (jobs[i][0] <= t or not heap):
                heapq.heappush(heap, (jobs[i][0] + jobs[i][1], jobs[i][0], jobs[i][0], jobs[i][1]))
                i += 1

    return total_response_time // N

print(solution([[0, 3], [1, 9], [2, 6]]))