# 입국심사
def solution(n, times):
    times.sort()
    l = 0
    r = n * times[-1]
    answer = r
    while l <= r:
        m = (l+r) // 2
        total = sum(m // time for time in times)

        if total < n:
            l = m + 1
        else:
            r = m - 1
            if m < answer:
                answer = m
    return answer
print(solution(6, [7, 10]))