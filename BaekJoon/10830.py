import sys


input = sys.stdin.readline


def matmul(A, B):
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += A[i][k] * B[k][j]
            arr[i][j] %= 1000
    return arr


N, B = map(int, input().split())
A = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]

An = A
An_list = [An]
two_n_list = [1]
n = 2
while n <= B:
    An = matmul(An, An)
    An_list.append(An)
    two_n_list.append(n)
    n *= 2

i = len(two_n_list) - 1
answer = An_list[i]
B -= two_n_list[i]
while B > 0 and i > 0:
    i -= 1
    if two_n_list[i] > B:
        continue

    answer = matmul(answer, An_list[i])
    B -= two_n_list[i]

for row in answer:
    print(*row)
