S = input().upper()
s = list(set(S))
s_count = []
max_count = 0

for x in s:
    count = 0
    for y in S:
        if x == y:
            count += 1
    s_count.append(count)
    if count > max_count:
        max_count = count
if s_count.count(max_count) > 1:
    print("?")
else:
    print(s[s_count.index(max_count)])
