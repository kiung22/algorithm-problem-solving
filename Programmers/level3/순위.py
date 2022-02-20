def solution(n, results):
    adj_winner = [[] for _ in range(n+1)]
    adj_loser = [[] for _ in range(n+1)]
    for winner, loser in results:
        adj_winner[winner].append(loser)
        adj_loser[loser].append(winner)
    
    
    def dfs(i, adj, cnt):
        for j in adj[i]:
            if not visited[j]:
                visited[j] = 1
                cnt = dfs(j, adj, cnt+1)
        return cnt


    answer = 0
    for i in range(1, n+1):
        visited = [0] * (n+1)
        win_cnt = dfs(i, adj_winner, 0)
        visited = [0] * (n+1)
        lose_cnt = dfs(i, adj_loser, 0)
        if win_cnt + lose_cnt == n - 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))