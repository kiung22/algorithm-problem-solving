roman = 'IV'

roman_digit = {'I': 1,   'V': 5,   'X': 10,  'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

roman = list(roman)
digit = []
for n in roman:
    digit.append(roman_digit[n])

print(digit)

for i in range(0, len(digit)-1):
    if digit[i] < digit[i+1]:
        digit[i] = -digit[i]

print(digit)
print(sum(digit))
