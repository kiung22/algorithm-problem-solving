def solution(rows, columns, queries):
    arr = [[i*columns + j for j in range(1, columns+1)] for i in range(rows)]
    
    answer = []
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        min_value = arr[x1][y1]

        for i in range(x1, x2):
            arr[i][y1], arr[i+1][y1] = arr[i+1][y1], arr[i][y1]
            min_value = min(min_value, arr[i][y1])

        for j in range(y1, y2):
            arr[x2][j], arr[x2][j+1] = arr[x2][j+1], arr[x2][j]
            min_value = min(min_value, arr[x2][j])

        for i in range(x2, x1, -1):
            arr[i][y2], arr[i-1][y2] = arr[i-1][y2], arr[i][y2]
            min_value = min(min_value, arr[i][y2])

        for j in range(y2, y1+1, -1):
            arr[x1][j], arr[x1][j-1] = arr[x1][j-1], arr[x1][j]
            min_value = min(min_value, arr[x1][j])

        answer.append(min_value)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))