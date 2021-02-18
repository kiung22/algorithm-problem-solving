N = int(input())
# set으로 중복 제거
words = list(set(input() for _ in range(N)))

# 문자열의 길이, 알파벳 순으로 정렬
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)