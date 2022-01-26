from collections import deque


def solution(n, results):
    indegree = [0] * (n+1)
    win = [[] for _ in range(n+1)]

    for u, v in results:
       win[u].append(v)
       indegree[v] += 1 

    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    answer = 0
    while queue:
        if len(queue) == 1:
            answer += 1

        queue2 = deque()
        while queue:
            u = queue.popleft()

            for v in win[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue2.append(v)
        queue = queue2

    return answer