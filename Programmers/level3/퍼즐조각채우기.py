from copy import deepcopy


d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(i, j, board, N, x, y, d_idx):
    block_indexs = [(i, j)]
    board[i][j] = y
    block = 1
    idx = 0
    while idx < len(block_indexs):
        i, j = block_indexs[idx]
        for di, dj in d[d_idx:]+d[:d_idx]:
            block <<= 1
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == x:
                block += 1
                block_indexs.append((ni, nj))
                board[ni][nj] = y
        idx += 1
    return block, block_indexs


def solution(game_board, table):
    N = len(game_board)
    blocks = {}

    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                block, block_indexs = dfs(i, j, game_board, N, 0, 1, 0)
                blocks[block] = blocks.get(block, 0) + len(block_indexs)

    tables = [deepcopy(table) for _ in range(4)]
    answer = 0
    for r in range(N):
        for c in range(N):
            for idx, (i, j) in enumerate([(r, c), (c, N-r-1), (N-r-1, N-c-1), (N-c-1, r)]):
                if tables[idx][i][j] == 1 and table[i][j] == 1:
                    block, block_indexs = dfs(i, j, tables[idx], N, 1, 0, idx)
                    n = len(block_indexs)
                    if block in blocks and blocks[block] > 0:
                        answer += n 
                        blocks[block] -= n
                        for i, j in block_indexs:
                            table[i][j] = 0
    return answer
