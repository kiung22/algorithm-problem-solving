def get_diff(start, end, n):
    result = end - start
    if result < 0:
        return result + n
    return result


def solution(n, weak, dist):
    W = len(weak)
    D = len(dist)

    for i in range(W):
        weak.append(n + weak[i])
    dist.sort(reverse=True)

    results = [range(W)]
    for i in range(D):
        d = dist[i]
        next_results = set()
        for result in results:
            tmp = set(result)
            idx = [w for w in range(W) if w in tmp]
            I = len(idx)
            end = 0
            start = 0
            while start < I:
                while tmp and get_diff(weak[idx[start]], weak[idx[end]], n) <= d:
                    tmp.discard(idx[end])
                    end = (end+1) % I
                if len(tmp) == 0:
                    return i + 1
                next_results.add(tuple(tmp))
                while start < I and get_diff(weak[idx[start]], weak[idx[end]], n) > d:
                    tmp.add(idx[start])
                    start += 1
        results = next_results

    return -1


print(solution(12, 	[1, 5, 6, 10], [1, 2, 3, 4]))
