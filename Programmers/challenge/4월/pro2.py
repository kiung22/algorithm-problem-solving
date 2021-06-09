def check(s):
    brackets = {
        '[': ']',
        '{': '}',
        '(': ')',
    }
    stack = []
    for i in s:
        if brackets.get(i):
            stack.append(brackets[i])
        else:
            if not stack or i != stack.pop():
                return 0
    if stack:
        return 0
    return 1

def solution(s):
    ans = 0
    for _ in range(len(s)):
        ans += check(s)
        s = s[1:] + s[0]
    return ans