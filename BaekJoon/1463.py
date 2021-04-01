N = int(input())

q = [N]
ans = -1

while q:
    qq, q = q, []
    ans += 1

    for n in qq:
        if n == 1:
            q = []
            break
        if not n % 3:
            q.append(n//3)
        if not n % 2:
            q.append(n//2)
        q.append(n-1)

print(ans)