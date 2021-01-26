# 튜플
def solution(s):
    s = eval(s.replace('{', '[').replace('}',']'))
    s.sort(key=lambda x: len(x))
    answer = [s[0][0]]

    for i in range(1, len(s)):
        answer.append(list(set(s[i])- set(s[i-1]))[0])

    return answer

"""
import re
from collections import Counter

def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
"""
