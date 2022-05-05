def solution(routes):
    routes.sort(key=lambda x: (x[0], -x[1]))
    
    end = 30001
    answer = 1
    for route in routes:
        if route[0] <= end:
            end = min(end, route[1])
        else:
            answer += 1
            end = route[1]
    return answer 
