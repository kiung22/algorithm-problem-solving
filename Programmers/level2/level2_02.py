# 기능개발
def solution(progresses, speeds):
    import math
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    day = days[0]
    count = 0
    answer = []
    for i in days:
        if i > day:
            day = i
            answer.append(count)
            count = 0
        count += 1
    if sum(answer) < len(days):
        answer.append(count)
    return answer

"""
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):   -> (3 // 2 = 1이지만 -3 // 2 = -2 이다.)
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
"""
