# 피보나치 수
def solution(n):
    fibonacci_numbers = [0]*(n+1)
    fibonacci_numbers[1] = 1
    if n > 1:
        for x in range(2, n+1):
            fibonacci_numbers[x] = fibonacci_numbers[x-1] + fibonacci_numbers[x-2]
    return fibonacci_numbers[n]%1234567

"""
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
"""
