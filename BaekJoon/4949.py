result = []

while True:
    # 입력
    text = input()

    # while문 종료조건
    if text == '.':
        break

    stack = []
    for t in text:
        # 열린 괄호이면 stack에 추가
        if t == '(':
            stack.append(')')
        elif t == '[':
            stack.append(']')
        
        # 닫힌 괄호이면 stack의 마지막 값과 확인
        elif t == ')' or t == ']':
            # stack이 비어있거나 마지막 원소가 t와 다르면 'no'
            if not(stack) or stack.pop() != t:
                result.append('no')
                break

    # 끝까지 순회했을 경우
    else:
        # stack에 괄호가 남아있다면 개수가 맞지 않으므로 'no'
        if stack:
            result.append('no')
        # stack이 비어있다면 'yes'
        else:
            result.append('yes')

# 출력
print(*result, sep='\n')
