# 구명보트
def solution(people, limit):
    people.sort(reverse=True)
    idx1 = 0
    idx2 = len(people) - 1
    count = 0

    while idx1 < idx2:
        if people[idx1] + people[idx2] <= limit:
            idx2 -= 1
        count += 1
        idx1 += 1

    if idx1 == idx2:
        count += 1

    return count
