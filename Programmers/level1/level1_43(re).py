# [1차] 다트 게임
def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    dR = []
    s = ''
    for i in dartResult:
        if i.isdigit() and len(s) > 1:
            dR.append(s)
            s = ''
        s += i
    dR.append(s)

    answer = []
    for x in dR:
        if not x[-1] in ('*', '#'):
            x += ' '
        answer.append(int(x[:-2])**bonus[x[-2]])

        if x[-1] == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif x[-1] == '#':
            answer[-1] *= -1

    return sum(answer)

"""
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
"""
