import sys

input = sys.stdin.readline 

N = int(input())
arr = list(map(int, input().split()))
s = sorted(list(set(arr)))

d = {}
for i, n in enumerate(s):
    d[n] = i

ans = []
for n in arr:
    ans.append(d[n])

print(*ans)