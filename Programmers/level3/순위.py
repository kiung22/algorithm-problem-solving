def solution(n, results):
    adj = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for winner, loser in results:
        adj[winner].append(loser)
        indegree[loser] += 1
    
    
    def dfs(i):
        for j in adj[i]:
            ranking[j] += 1
            print(i, j)
            dfs(j)
        return


    ranking = [1] * (n+1)

    for i in range(1, n+1):
        dfs(i)
    print(ranking)

    answer = 0
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))