def count_words(text, words):
    import string
    
    table = text.maketrans({key: None for key in string.punctuation})
    text = text.translate(table).lower()
    count = 0
    for word in words:
        if word in text:
            count +=1
    
    return count
