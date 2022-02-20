def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    up = [i-1 for i in range(n)]
    down = [i+1 for i in range(n)]
    stack = []
    for c in cmd:
        if c[0] == "U":
            num = int(c.split()[1])
            while num:
                k = up[k]
                num -= 1
        elif c[0] == "D":
            num = int(c.split()[1])
            while num:
                k = down[k]
                num -= 1
        elif c[0] == "C":
            answer[k] = "X"
            if up[k] >= 0:
                down[up[k]] = down[k]
            if down[k] < n:
                up[down[k]] = up[k]
            stack.append(k)
            k = down[k] if down[k] < n else up[k]
        else:
            num = stack.pop()
            answer[num] = "O"
            if up[num] >= 0:
                down[up[num]] = num
            if down[num] < n:
                up[down[num]] = num
    return "".join(answer)