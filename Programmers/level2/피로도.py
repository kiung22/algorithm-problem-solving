answer = 0

def solution(k, dungeons):
    global answer
    N = len(dungeons)
    visited = [0] * N

    def f(n, k, cnt):
        global answer
        if n == N or k == 0:
            answer = max(answer, cnt)
            return
        
        if cnt + N - n <= answer:
            return

        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                if k >= dungeons[i][0]:
                    f(n+1, k-dungeons[i][1], cnt+1)
                else:
                    f(n+1, k, cnt)
                visited[i] = 0
        return

    f(0, k, 0)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))