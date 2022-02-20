def rotate_array(array, d):
    n = len(array)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if d % 4 == 0:
                result[i][j] = array[i][j]
            elif d % 4 == 1:
                result[j][n-i-1] = array[i][j]
            elif d % 4 == 2:
                result[n-i-1][n-j-1] = array[i][j]
            else:
                result[n-j-1][i] = array[i][j]
    return result


def check(lock, n, m):
    for i in range(m, m+n):
        for j in range(m, m+n):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    N = len(lock)
    M = len(key)
    new_lock = [[0] * (N + M*2) for _ in range(N + M*2)]
    for i in range(N):
        for j in range(N):
            new_lock[i+M][j+M] = lock[i][j]
    
    for i in range(1, N+M):
        for j in range(1, N+M):
            for d in range(4):
                array = rotate_array(key, d)
                for r in range(M):
                    for c in range(M):
                        new_lock[r+i][c+j] += array[r][c]

                if check(new_lock, N, M):
                    return True
                
                for r in range(M):
                    for c in range(M):
                        new_lock[r+i][c+j] -= array[r][c]    
    return False
