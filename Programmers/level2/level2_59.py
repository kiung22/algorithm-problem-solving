def solution(dirs):
    visited = [[0] * 21 for _ in range(21)]
    di = {
        'U': -1,
        'D': 1,
        'R': 0,
        'L': 0
    }
    dj = {
        'U': 0,
        'D': 0,
        'R': 1,
        'L': -1
    }
    i = 10
    j = 10
    answer = 0
    for d in dirs:
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < 21 and 0 <= nj < 21:
            if visited[ni][nj] == 0:
                answer += 1
                visited[ni][nj] = answer
            i = ni + di[d]
            j = nj + dj[d]

    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))