import sys

input = sys.stdin.readline


def mat_mul(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000000007
    return result


def f(n):
    if n <= 1:
        return [[1, 1], [1, 0]]

    if n % 2:
        matrix = f(n-1)
        return mat_mul([[1, 1], [1, 0]], matrix)
    else:
        matrix = f(n//2)
        return mat_mul(matrix, matrix)


N = int(input().rstrip())

matrix = f(N-1)

print(matrix[0][0])