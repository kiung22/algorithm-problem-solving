from collections import deque


def is_convertible(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
            if count > 1:
                return False
    return True


def solution(begin, target, words):
    answer = 0
    queue = deque([begin])
    visited = [0] * len(words)
    while queue:
        temp_queue = deque()
        while queue:
            current_word = queue.popleft()
            if current_word == target:
                return answer
            for i in range(len(words)):
                if not visited[i] and is_convertible(current_word, words[i]):
                    visited[i] = 1
                    temp_queue.append(words[i])
        queue = temp_queue
        answer += 1
    return 0