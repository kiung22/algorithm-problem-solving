# 짝지어 제거하기
def solution(s):
    answer = []

    for alpha in s:
        if answer and answer[-1] == alpha:
            answer.pop()
        else:
            answer.append(alpha)
    return not(answer) and 1 or 0
