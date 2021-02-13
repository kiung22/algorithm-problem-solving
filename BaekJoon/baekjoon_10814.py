# 입력
N = int(input())
members = []
for _ in range(N):
    member = input().split()
    members.append((int(member[0]), member[1]))

result = sorted(enumerate(members), key=lambda x: (x[1][0], x[0]))
for i, (age, name) in result:
    print(age, name)