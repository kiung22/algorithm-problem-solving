def sign(n):
    cnt = 0
    if n ** 0.5 == int(n ** 0.5):
        return -1
    return 1

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        answer += n * sign(n)

    return answer