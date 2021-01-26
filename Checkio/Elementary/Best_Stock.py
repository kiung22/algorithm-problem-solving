def best_stock(data):
    max_price = 0
    answer = ''

    for s in data:
        if data[s] > max_price:
            max_price = data[s]
            answer = s
    
    return answer
