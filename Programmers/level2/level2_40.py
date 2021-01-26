# 영어 끝말잇기
def solution(n, words):
    arr = []
    for i, w in enumerate(words):
        print(w)
        if arr and (arr[-1][-1] != w[0] or w in arr):
            return [i%n + 1, i//n + 1]
        arr.append(w)
    return [0, 0]

"""
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
"""
