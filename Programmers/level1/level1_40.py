# 예산
def solution(d, budget):
    count = 0
    for i in sorted(d):
        budget -= i
        if budget < 0:
            break
        count += 1
    return count
