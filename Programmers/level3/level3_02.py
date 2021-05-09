# N으로 표현
def solution(N, number):
    if N == number:
        return 1

    S = [{N}]
    n = N
    for k in range(2, 9):
        S_k = set()
        n *= 10
        n += N
        S_k.add(n)
        for i in range(k//2):
            j = k-i-2
            for p in S[i]:
                for q in S[j]:
                    for r in [p+q, p-q, q-p, p*q, p//q, q//p]:
                        if r > 0:
                            S_k.add(r)

        if number in S_k:
            return k
        S.append(S_k)

    return -1
