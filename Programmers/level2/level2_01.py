# 멀쩡한 사각형
def solution(w, h):
    import math
    return (w * h) - (w + h - math.gcd(w, h))
