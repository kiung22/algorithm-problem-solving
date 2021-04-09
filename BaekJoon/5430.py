import sys

input = sys.stdin.readline

def R():
    global d

    if d:
        d = 0
    else:
        d = 1

def D():
    global l, r, d
    
    if d:
        r -= 1
    else:
        l += 1
    
    if l > r+1:
        return 1
    return 0

def solve():
    for q in p:
        if q == 'R':
            R()
        else:
            if D():
                print('error')
                return
    
    ans = []
    if d:
        for i in range(r, l-1, -1):
            ans.append(str(arr[i]))
    else:
        for i in range(l, r+1):
            ans.append(str(arr[i]))
    print('[' + ','.join(ans) + ']')

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = eval(input().rstrip())
    
    d = 0   # 0이면 왼쪽에서 오른쪽, 1이면 오른쪽에서 왼쪽
    l = 0
    r = n-1    

    solve()
        