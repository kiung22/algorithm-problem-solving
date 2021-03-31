# 하노이 탑 이동 순서
N = int(input())
A = 1
B = 3
arr = []

def solution(N, A, B, arr):
    C = 6 - (A + B)
    if N == 1:
        arr.append((A, B))
        return None
    solution(N - 1, A, C, arr)
    arr.append((A, B))
    solution(N - 1, C, B, arr)

solution(N, A, B, arr)

print(len(arr))
for n, m in arr:
    print(n, m)