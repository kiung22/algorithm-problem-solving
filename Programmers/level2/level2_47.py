# 후보키
from itertools import combinations

def solution(relation):
    temp = []

    for k in range(1, len(relation[0])+1):
        for c in combinations(range(len(relation[0])), k):
            if len({tuple([r[i] for i in c]) for r in relation}) == len(relation):
                if temp:
                    for i in temp:
                        if not set(i)-set(c):
                            break
                    else:
                        temp.append(c)
                else:
                    temp.append(c)

    return len(temp)
