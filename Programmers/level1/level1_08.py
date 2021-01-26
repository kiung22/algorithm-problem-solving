# 3진법 뒤집기
def solution(n):
    n3 = []
    while n:
        n, r = divmod(n, 3)
        n3.append(r)

    for i, x in enumerate(reversed(n3)):
        n += x * 3**i

    return n
