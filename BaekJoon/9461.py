import sys

input = sys.stdin.readline

def P(N):
    arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for i in range(11, N+1):
        arr.append(arr[i-1] + arr[i-5])
    
    return arr[N]

T = int(input())
for _ in range(T):
    N = int(input())

    print(P(N))