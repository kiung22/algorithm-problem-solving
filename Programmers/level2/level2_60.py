def get_avgs(scores):
    N = len(scores)

    avgs = [0] * N
    for i in range(N):
        my_score = scores[i][i]
        min_score = 100
        max_score = 0
        for j in range(N):
            if j == i: continue
            min_score = min(min_score, socres[i][j])
            max_score = max(max_score, socres[i][j])
            avgs[i] += scores[i][j]
        
        if min_score <= my_score <= max_score:
            avgs[i] += my_score
            avgs[i] //= N
        else:
            avgs[i] //= N - 1
    return avgs

def solution(scores):
    avgs = get_avgs(scores)

    

    answer = ''
    return answer