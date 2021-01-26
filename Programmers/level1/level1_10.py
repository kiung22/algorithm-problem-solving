# 같은 숫자는 싫어
def solution(arr):
    answer = []
    for x in arr:
        if len(answer) == 0 or x != answer[-1]:
            answer.append(x)
    return answer

"""
def no_continuous(s):
    return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]
"""
