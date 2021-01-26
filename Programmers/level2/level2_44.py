# [1차] 캐시
def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = {}
    time = 0
    for city in cities:
        if city in cache:
            time += 1
        else:
            time += 5

        cache[city] = -1
        for key in cache:
            cache[key] += 1

        if len(cache) > cacheSize:
            del cache[max(cache, key=lambda x: cache[x])]

    return time

"""
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
"""
