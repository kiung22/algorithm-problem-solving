def find(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    if x < y:
        p[y] = x
    else:
        p[x] = y
    return


def solution(n, costs):
    global p

    answer = 0
    p = [i for i in range(n)]
    costs.sort(key= lambda x: x[2])
    count = 0
    for u, v, w in costs:
        u_p = find(u)
        v_p = find(v)
        if u_p != v_p:
            union(u_p, v_p)
            answer += w
            count += 1
            if count == n-1:
                return answer
