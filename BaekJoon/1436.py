N = int(input())

cnt = 0
number = 665
# cnt가 N과 같아지면 while문 종료
while cnt < N:
    # 숫자를 1씩 증가
    number += 1

    # 숫자에 666이 들어있으면 cnt를 1씩 증가
    if '666' in str(number):
        cnt += 1

print(number)