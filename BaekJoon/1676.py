# N! 구하기
def factorial(n):
    ans = 1
    i = 1
    while i <= N:
        ans *= i
        i += 1
    return ans

# 뒤에서부터 0이 아닌 수가 나올 때까지 0의 개수 세기
def count_zero(n):
    cnt = 0
    while True:
        r = n % 10
        if r == 0:
            cnt += 1
        else:
            break
        n //= 10
    return cnt

N = int(input())
print(count_zero(factorial(N)))