croatiaAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = 0

for c in croatiaAlpha:
    count += word.count(c)
    word = word.replace(c, " ")

count += len(word.replace(" ", ""))
print(count)
