# 이진 변환 반복하기
def solution(s):
    count = 0
    zeros = 0
    while s != '1':
        zeros += s.count('0')
        count += 1
        s = bin(len(s)-s.count('0'))[2:]    
    return [count, zeros]

print(solution("1111111"))
