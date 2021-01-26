def 한수(n):
    n1 = n//100
    n2 = (n - n1*100)//10
    n3 = (n - n1*100 - n2*10)
    return n1 - n2 == n2 - n3


N = int(input())
if N < 100:
    print(N)
else:
    result = 99
    for i in range(100, N + 1):
        result += 한수(i)
    print(result)
