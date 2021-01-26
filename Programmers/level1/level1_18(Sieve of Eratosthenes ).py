# 소수 찾기
def solution(n):
    prime = [True] * (n+1)

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    primeNumbers = [i for i in range(2, n+1) if prime[i] == True]
    return len(primeNumbers)

"""
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, int(n**0.5)+1):
        if i in num:
            num -= set(range(i**2,n+1,i))
    return len(num)
"""
