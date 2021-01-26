# 실패율
def solution(N, stages):
    rate = []
    player = len(stages)
    for i in range(1, N+1):
        x = stages.count(i)
        if player:
            rate.append([i, x/player])
            player -= x
        else:
            rate.append([i, 0])

    return [x[0] for x in sorted(rate, reverse=True, key=lambda x: x[1])]
