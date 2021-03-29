def f(A, B, cnt):
    global ans
    if A == B:
        ans = cnt
        return
    if A > B:
        ans = -1
        return

    if B % 10 == 1:
        f(A, B // 10, cnt + 1)
    elif B % 2 == 0:
        f(A, B // 2, cnt + 1)
    else:
        ans = -1
        return


A, B = map(int, input().split())

f(A, B, 1)

print(ans)