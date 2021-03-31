# 입력
N = int(input())
members = []
for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))

result = sorted(members, key=lambda x: (x[0]))
for age, name in result:
    print(age, name)