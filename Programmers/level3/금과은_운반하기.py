def solution(a, b, g, s, w, t):
    N = len(g)
    start = 0 
    end = 10**5 * (4 * 10**9 - 1)
    answer = end
    while start < end:
        mid = (end+start) // 2
        g_max = 0
        g_min = 0
        s_max = 0
        s_min = 0
        for i in range(N):
            n = (mid//t[i] + 1) // 2
            g_max += g[i] if g[i] < n*w[i] else n*w[i]
            s_min += min(s[i], n*w[i] - g[i]) if g[i] < n*w[i] else 0
            s_max += s[i] if s[i] < n*w[i] else n*w[i]
            g_min += min(g[i], n*w[i] - s[i]) if s[i] < n*w[i] else 0
        
        if a <= g_max and b <= s_max and a+b <= g_max+s_min:
            answer = min(answer, mid)
            end = mid
        else:
            start = mid + 1
    return answer
