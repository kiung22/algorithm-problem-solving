# 체육복
from collections import Counter
def solution(n, lost, reserve):
    lost_reserve = Counter(lost) + Counter(reserve)
    both = [x for x in list(lost_reserve) if lost_reserve[x] == 2]

    for x in both:
        lost.remove(x)
        reserve.remove(x)
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r-1)
        elif r + 1 in lost:
            lost.remove(r+1)

    return n - len(lost)

"""
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
"""
