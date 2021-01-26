# 별 찍기 - 10

N = int(input())
stars = [[' ' if i == 1 and j == 1 else '*' for j in range(3)] for i in range(3)]

def solution(N, stars=stars):
    if N == 3:
        return stars
    
    n = N // 3
    if len(stars) < n:
        stars = solution(n)
    temp = []
    for i in range(N):
        if n <= i < 2 * n:
            temp.append(stars[i % n] + [' '] * n + stars[i % n])
        else:
            temp.append(stars[i % n] * 3)
    stars = temp
    return stars

result = solution(N)
for s in result:
    print(''.join(s))