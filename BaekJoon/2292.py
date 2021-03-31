N = int(input())

def solution(N):
    cnt = 1
    total = 1
    while True:
        if total >= N:
            return cnt
        total += 6 * cnt
        cnt += 1
        

print(solution(N))