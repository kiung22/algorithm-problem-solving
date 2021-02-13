N = int(input())

for _ in range(N):
    PS = input()
    open_cnt = 0
    close_cnt = 0
    for p in PS:
        if p == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        if close_cnt > open_cnt:
            break
    if open_cnt == close_cnt:
        print('YES')
    else:
        print('NO')