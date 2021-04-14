import sys

input = sys.stdin.readline 

def f(n, channel):
    global ans 

    if n == 0:
        ans = min(ans, abs(N - channel) + len(str(channel)))
        return 

    for button in buttons:
        f(n-1, channel*10 + button)


N = int(input())
M = int(input())

N_length = len(str(N))
if M:
    broken = set(map(int, input().split()))
    buttons = [i for i in range(10) if i not in broken]
    ans = abs(N - 100)

    s = max(N_length-1, 1)
    for i in range(s, N_length+2):
        f(i, 0)

    print(ans)
else:
    print(min(N_length, abs(N - 100)))