def solution(a):
    N = len(a)
    count = [0] * N
    used = [-1] * N

    for i in range(N):
        if i-1 >= 0 and a[i-1] != a[i] and used[a[i]] < i-1:
            count[a[i]] += 1
            used[a[i]] = i-1
        elif i+1 < N and a[i+1] != a[i] and used[a[i]] < i+1:
            count[a[i]] += 1
            used[a[i]] = i+1

    return max(count) * 2