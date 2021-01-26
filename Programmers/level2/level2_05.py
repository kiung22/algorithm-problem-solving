# 124 나라의 숫자
def solution(n):
    if n - 1 < 3:
        return '124'[n - 1]
    else:
        q = (n - 1) // 3
        r = (n - 1) % 3             # q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]
