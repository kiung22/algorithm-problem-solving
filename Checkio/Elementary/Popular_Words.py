def popular_words(text, words):

    answer = {}
    text = text.lower()
    splitted_words = text.split()
    
    for word in words:
        answer[word] = splitted_words.count(word)

    return answer
