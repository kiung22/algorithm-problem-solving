r = 31
M = 1234567891
L = int(input())
string = input()

hash_value = 0
for i in range(L):
    hash_value += (ord(string[i]) - 96) * r**i
hash_value %= M
print(hash_value)