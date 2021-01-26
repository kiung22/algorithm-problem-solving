# [1차] 비밀지도
def solution(n, arr1, arr2):
    arr1_ = [format(x, 'b').zfill(n) for x in arr1]
    arr2_ = [format(x, 'b').zfill(n) for x in arr2]

    return [''.join(["#" if int(c)+int(d) else " " for c, d in zip(a, b)]) for a, b in zip(arr1_, arr2_)]

"""
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])        비트 연산자
        answer.append(a12.rjust(n,'0').replace('1','#').replace('0',' '))
    return answer
"""
