# 풍선 터트리기
def solution(a):
    left = []
    for i in a:
        if not left or left[-1]>i:
            left.append(i)
        else:
            left.append(left[-1])
    right = []
    for i in reversed(a):
        if not right or right[-1]>i:
            right.append(i)
        else:
            right.append(right[-1])
    right.reverse()

    answer = 0
    for x, l, r in zip(a, left, right):
        if x > l and x > r:
            continue
        answer += 1
    return answer

"""
def solution(a):
    m = 1000000001
    n = 1000000001
    l = [(m := min(m, v)) for v in a[:-1]]
    r = [(n := min(n, v)) for v in reversed(a[2:])]
    return sum((x > y or z > y for x, y, z in zip(l, a[1:-1], reversed(r)))) + 2
"""
