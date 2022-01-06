import sys

input = sys.stdin.readline


board = [list(map(int, input().rstrip())) for _ in range(9)]

zeros = []
rows = [[0] * 10 for _ in range(9)]
colums = [[0] * 10 for _ in range(9)]
rects = [[0] * 10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))
        else:
            rows[i][board[i][j]] = 1
            colums[j][board[i][j]] = 1
            rects[i//3*3 + j//3][board[i][j]] = 1

def check_number(n, num):
    i, j = zeros[n]
    if rows[i][num] == 0 and colums[j][num] == 0 and rects[i//3*3 + j//3][num] == 0:
        return True
    return False

def write_number(n, num):
    i, j = zeros[n]
    board[i][j] = num
    rows[i][num] = 1
    colums[j][num] = 1
    rects[i//3*3 + j//3][num] = 1
    return

def erase_number(n):
    i, j = zeros[n]
    rows[i][board[i][j]] = 0
    colums[j][board[i][j]] = 0
    rects[i//3*3 + j//3][board[i][j]] = 0
    board[i][j] = 0
    return

def sudoku(n):
    global finish

    if finish:
        return

    if n == len(zeros):
        for i in range(9):
            print(*board[i], sep='')
        finish = True
        return
    
    for num in range(1, 10):
        if check_number(n, num):
            write_number(n, num)
            sudoku(n+1)
            erase_number(n)

finish = False
sudoku(0)
