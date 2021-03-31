import sys

N = int(sys.stdin.readline())
input_data = map(int, [sys.stdin.readline() for _ in range(N)])

number = 1
stack = []
ans = []    # 출력할 '+', '-'을 담을 list
for n in input_data:
    # numbers의 마지막 원소가 입력받은 n 보다 커질때까지 stack에 push한다.
    while number <= n:
        stack.append(number)
        number += 1
        ans.append('+')

    # stack pop의 결과가 n과 같으면 성공, 다르면 불가능이므로 'No'를 출력하고 종료
    if stack[-1] == n:
        stack.pop()
        ans.append('-')
    else:
        ans = ['NO']
        break

for a in ans:
    print(a)