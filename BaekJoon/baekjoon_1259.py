while True:
    N = input()

    # 0을 입력받을 때까지 반복
    if N == '0':
        break

    # 입력받은 수와 순서를 뒤집은 수가 같으면 yes
    if N == N[::-1]:
        print('yes')
    # 다르면 no
    else:
        print('no')