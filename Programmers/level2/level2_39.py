# 점프와 순간이동
def solution(n):
    count = 0
    while n > 2:
        n, r = divmod(n, 2)
        if r:
            count += 1
    count += 1
    return count

# def solution(n): return bin(n).count('1')
