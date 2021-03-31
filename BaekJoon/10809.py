from string import ascii_lowercase
S = input()

alpha_list = list(ascii_lowercase)
alphabet = []
for alpha in alpha_list:
    if alpha in S:
        alphabet.append(str(S.index(alpha)))
    else:
        alphabet.append(str(-1))

print(" ".join(alphabet))
