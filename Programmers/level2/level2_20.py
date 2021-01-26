# 카펫
def solution(brown, yellow):
    total = brown + yellow
    for y in range(3, total//3+1):
        x, n = divmod(total, y)
        if not n:
            if (x-2)*(y-2) == yellow:
                return [x, y]
