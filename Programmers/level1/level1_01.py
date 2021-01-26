# 크레인 인형뽑기 게임
def solution(board, moves):
    basket = []
    count = 0

    for m in moves:
        for b in board:
            if b[m - 1]:
                basket.append(b[m - 1])
                b[m - 1] = 0
                if len(basket) >= 2:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        count += 2
                break

    return count
