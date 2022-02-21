import re


def solution(user_id, banned_id):
    banned_pattern = list(map(lambda x: "^" + x.replace("*", ".") + "$", banned_id))
    banned_set = set()
    visited = [0] * len(user_id)


    def f(n):
        if n == len(banned_id):
            banned_set.add(tuple(visited))
            return
        for i in range(len(user_id)):
            if visited[i] == 0 and re.match(banned_pattern[n], user_id[i]):
                visited[i] = 1
                f(n+1)
                visited[i] = 0


    f(0)
    answer = len(banned_set)
    return answer