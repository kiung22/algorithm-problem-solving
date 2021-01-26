# [카카오 인턴] 수식 최대화
import re
import itertools
def solution(expression):
    p = re.compile('[\+\-\*]')
    operator = set(p.findall(expression))
    answer = []
    for o in itertools.permutations(operator, len(operator)):
        e = expression
        _ = False
        for x in o:
            if x == '-':
                _ = True
            if _:
                p = re.compile(f'\-?\d+\{x}\-?\d+')
            else:
                p = re.compile(f'\d+\{x}\d+')
            while p.search(e):
                n = p.search(e).group()
                m = str(eval(n))
                e = e.replace(n, m)

        answer.append(abs(int(e)))
    return max(answer)

"""
import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [y for y in permutations(op)]
    ex = re.split('(\D)',expression)       ### '\D'로 split할 경우에는 +,-,*가 리스트에 포함되지 않지만
                                           ### '(\D)'로 하면 리스트에 +,-,*가 포함된다
    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)
"""
