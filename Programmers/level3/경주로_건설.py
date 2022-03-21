import heapq


D = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(board):
    N = len(board)
    heap = [(-500, -5, 0, 0)]
    cost_arr = [[[0] * 4 for _ in range(N)] for _ in range(N)]

    while heap:
        cost, cd, i, j = heapq.heappop(heap)

        for nd in range(4):
            if abs(cd - nd) == 2: continue
            di, dj = D[nd]
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                if cd == nd:
                    next_cost = cost + 100
                else:
                    next_cost = cost + 600
                if cost_arr[ni][nj][nd] == 0 or next_cost < cost_arr[ni][nj][nd]:
                    cost_arr[ni][nj][nd] = next_cost
                    heapq.heappush(heap, (next_cost, nd, ni, nj))
    return min(cost for cost in cost_arr[N-1][N-1] if cost)