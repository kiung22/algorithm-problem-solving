import sys

input = sys.stdin.readline 


N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

end = 0
ans = 0
for s, e in meetings:
    if s >= end:
        ans += 1
        end = e

print(ans)
    