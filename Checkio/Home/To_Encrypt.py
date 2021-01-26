def to_encrypt(text, delta):
    from string import ascii_lowercase
    
    alpha = ascii_lowercase
    table = text.maketrans(alpha, alpha[delta:] + alpha[:delta])
    answer = text.translate(table)
    return answer
