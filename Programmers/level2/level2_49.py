# [3차] 압축
from string import ascii_uppercase
def solution(msg):
    hash = dict(zip(ascii_uppercase, range(1, 27)))
    answer = []
    w = 0
    c = 2
    i = 26
    while w < len(msg):
        while c <= len(msg) and msg[w:c] in hash:
            c += 1
        answer.append(hash[msg[w:c-1]])
        i += 1
        hash[msg[w:c]] = i
        w = c - 1
        c = w + 2

    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))
