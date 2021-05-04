from collections import deque

def check(s):
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []
    for p in s:
        if pairs.get(p):
            stack.append(pairs[p])
        else:
            if len(stack) > 0 and p == stack[-1]:
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    return 1
            

def solution(s):
    q = deque(s)

    answer = 0
    for _ in range(len(s)):
        answer += check(''.join(q))
        q.append(q.popleft())
        
    return answer

print(solution("}]()[{"))