# 모의고사
def solution(answers):
    stu1 = "12345"
    stu2 = "21232425"
    stu3 = "3311224455"
    students = [stu1, stu2, stu3]
    count = {stu1: 0, stu2: 0, stu3: 0}

    for i in range(len(answers)):
        for stu in students:
            if int(stu[i%len(stu)]) == answers[i]:
                count[stu] += 1
    print(count)

    return [int(i[0]) for i in count if count[i] == max(count.values())]

"""
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
"""
