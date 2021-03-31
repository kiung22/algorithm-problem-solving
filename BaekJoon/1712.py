# A = 고정비용
# B = 가변비용
# C = 가격
A, B, C = map(int, input().split())

def solution(A, B, C):
    # 손익분기점이 존재하지 않을 때
    if C <= B:
        return -1

    # 손익분기점이 존재할 떄
    return A // (C - B) + 1

print(solution(A, B, C))