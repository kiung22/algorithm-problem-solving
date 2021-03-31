N = int(input())
words = [input() for x in range(N)]
count = 0

for word in words:
    group_count = 0
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            group_count += 1

    if group_count + 1 == len(set(word)):
        count += 1

print(count)
