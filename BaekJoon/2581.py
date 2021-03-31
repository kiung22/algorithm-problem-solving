M = int(input())
N = int(input())

prime_numbers = []
for n in range(M, N + 1):
    if n == 1:
        continue
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            break
    else:
        prime_numbers.append(n)

if prime_numbers:
    print(sum(prime_numbers))
    print(prime_numbers[0])
else:
    print(-1)