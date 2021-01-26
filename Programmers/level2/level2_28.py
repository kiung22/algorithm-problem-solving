# 숫자의 표현
def solution(n):
    answer = 0
    #i(2*x+i-1)/2=n
    for i in range(1, n):
        x = (2*n/i-(i-1))/2
        if x>0 and x%1 == 0:
            answer += 1
    return answer

"""
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
"""
