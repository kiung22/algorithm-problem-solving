def solution(m, n, puddles):
    arr = [[0] * (m+1) for _ in range(n+1)]
    arr[1][1] = 1
    for i, j in puddles:
        arr[j][i] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j] == -1:
                continue
            arr[i][j] += max(arr[i-1][j], 0) + max(arr[i][j-1], 0)
            arr[i][j] %= 1000000007
    answer = arr[n][m]
    return answer
