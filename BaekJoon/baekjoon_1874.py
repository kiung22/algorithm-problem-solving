N = int(input())

number = 1
stack = []
ans = ''    # 출력할 '+', '-'을 담을 변수
for _ in range(N):
    n = int(input())

    # numbers의 마지막 원소가 입력받은 n 보다 커질때까지 stack에 push한다.
    while number <= n:
        stack.append(number)
        number += 1
        ans += '+'

    # stack pop의 결과가 n과 같으면 성공, 다르면 불가능이므로 'No'를 출력하고 종료
    if stack.pop() == n:
        ans += '-'
    else:
        print('No')
        break

# for문이 break되지 않았다면 ans 출력
else:
    print(*ans, sep='\n')