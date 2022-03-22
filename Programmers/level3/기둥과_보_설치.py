# 보가 조건을 만족하는지 확인하는 함수
def check_beam(x, y):
    if (board[y-1][x][0] or board[y-1][x+1][0]) or (board[y][x-1][1] and board[y][x+1][1]):
        return True
    return False


# 기둥이 조건을 만족하는지 확인하는 함수
def check_column(x, y):
    if board[y-1][x][0] or board[y][x][1] or board[y][x-1][1]:
        return True
    return False


def solution(n, build_frame):
    global board

    board = [[[0, 0] for _ in range(n+3)] for _ in range(n+3)]
    for i in range(1, n+2):
        board[0][i][0] = 1

    for x, y, a, b in build_frame:
        x += 1
        y += 1
        if a == 0:
            # 기둥
            if b == 1:
                # 설치
                if check_column(x, y):
                    board[y][x][0] = 1
            else:
                # 삭제
                board[y][x][0] = 0
                if board[y+1][x][0] and not(check_column(x, y+1)):
                    board[y][x][0] = 1
                elif board[y+1][x][1] and not(check_beam(x, y+1)):
                    board[y][x][0] = 1
                elif board[y+1][x-1][1] and not(check_beam(x-1, y+1)):
                    board[y][x][0] = 1
        else:
            # 보
            if b == 1:
                # 설치
                if check_beam(x, y):
                    board[y][x][1] = 1
            else:
                # 삭제
                board[y][x][1] = 0
                if board[y][x][0] and not(check_column(x, y)):
                    board[y][x][1] = 1
                elif board[y][x+1][0] and not(check_column(x+1, y)):
                    board[y][x][1] = 1
                elif board[y][x+1][1] and not(check_beam(x+1, y)):
                    board[y][x][1] = 1
                elif board[y][x-1][1] and not(check_beam(x-1, y)):
                    board[y][x][1] = 1
    
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if board[j+1][i+1][k]:
                    answer.append([i, j, k])
    return answer