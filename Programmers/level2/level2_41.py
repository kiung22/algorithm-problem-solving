# 예상 대진표
from math import log
def solution(n, a, b):
    log2 = int(log(n, 2))
    span = range(1, n+1)
    count = -1
    for i in range(log2):
        count += 1
        span1 = span[:len(span)//2]
        span2 = span[len(span)//2:]
        if a in span1 and b in span1:
            span = span1
        elif a in span2 and b in span2:
            span = span2
        else:
            break
    return log2 - count

# def solution(n,a,b): return ((a-1)^(b-1)).bit_length()

"""
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
"""
