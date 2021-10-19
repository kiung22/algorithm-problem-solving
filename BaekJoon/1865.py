import sys

input = sys.stdin.readline


# 벨만-포드 알고리즘
# 음수 가중치가 있을 때에도 사용
def bellman_ford(n):
    dist = [INF] * N
    dist[n] = 0

    # edge relaxation을 V-1번 반복
    for _ in range(N-1):
        for w, u, v in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    # negative cycle이 있는지 확인
    for w, u, v in edges:
        if dist[v] > dist[u] + w:
            return True
    return False


T = int(input())
for _ in range(T):
    # N: 지점의 수, M: 도로의 수, W: 웜홀의 수
    N, M, W = map(int, input().split())

    adj = [[0] * N for _ in range(N)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        if adj[s-1][e-1] == 0 or adj[s-1][e-1] > t:
            adj[s-1][e-1] = t
            adj[e-1][s-1] = t
    wormholes = []
    for _ in range(W):
        s, e, t = map(int, input().split())
        adj[s-1][e-1] = -t
        wormholes.append(s-1)

    edges = []
    for i in range(N):
        for j in range(N):
            if adj[i][j] != 0:
                edges.append((adj[i][j], i, j))
    
    INF = 1000000000000000
    if bellman_ford(0):
        print('YES')
    else:
        print('NO')