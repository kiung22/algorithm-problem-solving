def most_frequent(data):
    dict_count = {}
    n = 0
    for word in data:
        dict_count[word] = data.count(word)
    for i in dict_count.keys():
        if dict_count[i] > n:
            n = dict_count[i]
            m = i
    return m
