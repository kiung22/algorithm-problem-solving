def get_avgs(scores):
    N = len(scores)

    avgs = [0] * N
    for i in range(N):
        my_score = scores[i][i]
        min_score = 100
        max_score = 0
        for j in range(N):
            if j == i: continue
            min_score = min(min_score, scores[j][i])
            max_score = max(max_score, scores[j][i])
            avgs[i] += scores[j][i]
        
        if min_score <= my_score <= max_score:
            avgs[i] += my_score
            avgs[i] //= N
        else:
            avgs[i] //= N - 1
    return avgs

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 50:
        return 'D'
    return 'F'

def solution(scores):
    avgs = get_avgs(scores)

    answer = ''
    for avg in avgs:
        answer += get_grade(avg)

    return answer