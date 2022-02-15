def solution(n, info):
    global score_diff, answer

    apeach_score = sum(i for i in range(11) if info[10-i])
    score_diff = 0
    visited = [0] * 11
    answer = [0] * 11
    
    def f(ryan_score, apeach_score, n):
        global score_diff, answer

        if ryan_score - apeach_score > score_diff:
            score_diff = ryan_score - apeach_score
            answer = visited[::-1]
            answer[-1] = n


        for i in range(1, 11):
            if not visited[i]:
                if info[10-i] + 1 > n:
                    continue
                visited[i] = info[10-i] + 1
                if info[10-i]:
                    f(ryan_score+i, apeach_score-i, n-info[10-i]-1)
                else:
                    f(ryan_score+i, apeach_score, n-info[10-i]-1)
                visited[i] = 0
        return
    
    f(0, apeach_score, n)
    if score_diff:
        return answer
    return [-1]
