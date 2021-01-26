# 올바른 괄호
def solution(str):
    open = 0
    close = 0
    for s in str:
        if s == '(':
            open += 1
        else:
            close += 1
        if close > open:
            return False
    return close == open
