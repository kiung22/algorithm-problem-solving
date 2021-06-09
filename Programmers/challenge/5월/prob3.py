def solution(s):
    answer = []
    for x in s:
        y = ''
        i = 0
        cnt = 0
        stack = []
        cnt = 0
        for i in x:
            if i == '1':
                stack.append(i)
            else:
                if len(stack) < 2:
                    y += ''.join(stack) + i
                    stack = []
                else:
                    stack.pop()
                    stack.pop()
                    cnt += 1
        y += '110'*cnt
        y += '1'*len(stack)
        answer.append(y)
            
    return answer

print(solution(['111110', '11000111', '11111000', '01011001100']))