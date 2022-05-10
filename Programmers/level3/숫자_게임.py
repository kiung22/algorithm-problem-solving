def solution(A, B):
    A.sort()
    B.sort()

    i = 0
    N = len(A)
    answer = 0
    for b in B:
        if b > A[i]:
            answer += 1
            i += 1
    return answer