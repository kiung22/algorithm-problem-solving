import sys

N, M = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(N):
    set1.add(sys.stdin.readline().rstrip())

for _ in range(M):
    set2.add(sys.stdin.readline().rstrip())

persons = list(set1 & set2)
persons.sort()

print(len(persons))
for person in persons:
    print(person)
