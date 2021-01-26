def bigger_price(limit, data):
    
    return  sorted(data, key=lambda x: x['price'], reverse=True)[:limit]
