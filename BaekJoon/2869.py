A, B, V = map(int,input().split())

print((V - A)//(A - B) + 1 + bool((V - A)%(A - B)))