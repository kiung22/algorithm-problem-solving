# [1차] 프렌즈4블록
def solution(m, n, board):
    board = [[board[j][i] for j in range(m-1, -1, -1)] for i in range(n)]
    count = 0

    while True:
        index_list = []
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == '0':
                    continue
                if board[i][j]*3 == board[i][j+1] + board[i+1][j] + board[i+1][j+1]:
                    index_list.append((i, j))

        if not index_list:
            break

        for i, j in index_list:
            board[i][j] = ''
            board[i+1][j] = ''
            board[i][j+1] = ''
            board[i+1][j+1] = ''

        board_ = [list(''.join(b)) for b in board]
        for b, b_ in zip(board, board_):
            x = len(b) - len(b_)
            count += x
            for i in range(x):
                b_.append('0')

        board = board_

    return count

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
