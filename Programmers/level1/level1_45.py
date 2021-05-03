def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    cnt = 0
    for n in win_nums:
        if n in lottos:
            cnt += 1
    
    answer = [rank[cnt_0 + cnt], rank[cnt]]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))