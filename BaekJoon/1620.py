import sys

N, M = map(int, input().split())

pokemon1 = {}
pokemon2 = []
for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    pokemon1[name] = i
    pokemon2.append(name)

for _ in range(M):
    question = sys.stdin.readline().rstrip()

    if question.isdigit():
        i = int(question)-1
        print(pokemon2[i])
    else:
        print(pokemon1[question])
