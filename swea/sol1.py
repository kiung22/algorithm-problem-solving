import sys

sys.stdin = open('input.txt')

def startpoint():
    for i in range(N):
        for j in range(M-1, 54, -1):
            if arr[i][j] == '1':
                return i, j-55

def solution():
    i, j = startpoint()
    code = []
    for k in range(8):
        s = arr[i][j+k*7:j+k*7+7]
        code.append(code_dict[s])
    
    x = (10 - (code[0]+code[2]+code[4]+code[6])*3 - (code[1]+code[3]+code[5]))%10
    if x == code[7]:
        return sum(code)
    return 0


code_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {solution()}')