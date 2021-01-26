# 소수 만들기
from itertools import combinations

def prime(n):
    num = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in num:
            num -= set(range(i**2,n+1,i))
    return num

def solution(nums):
    sumNums = list(map(sum, combinations(nums, 3)))
    primeNums = prime(max(sumNums))
    count = 0
    for n in sumNums:
        if n in primeNums:
            count += 1
    return count
