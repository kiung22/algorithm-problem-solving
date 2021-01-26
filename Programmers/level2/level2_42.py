# [1차] 뉴스 클러스터링
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    mset1 = [str1[i] + str1[i+1] for i in range(len(str1)-1) if (str1[i] + str1[i+1]).isalpha()]
    mset2 = [str2[i] + str2[i+1] for i in range(len(str2)-1) if (str2[i] + str2[i+1]).isalpha()]
    intersection = 0
    for s in set(mset1)&set(mset2):
        intersection += min([mset1.count(s), mset2.count(s)])
    union = len(mset1)+len(mset2)-intersection

    return int(intersection/union * 65536) if union else 65536

"""
from collections import Counter
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)  # Counter는 교집합 합집합 가능
    return answer
"""
