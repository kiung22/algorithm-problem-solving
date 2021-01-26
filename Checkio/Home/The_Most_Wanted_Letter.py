def checkio(text):
    text = sorted(list(text.lower()))
    dict_count = {}
    n = 0
    for letter in text:
        dict_count[letter] = text.count(letter)
    for i in dict_count.keys():
        if i.isalpha():
            if dict_count[i] > n:
                n = dict_count[i]
                m = i
    return m
