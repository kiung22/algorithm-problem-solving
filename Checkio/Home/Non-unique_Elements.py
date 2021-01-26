def checkio(data):
    list_unique_int = []
    for int in data:
        if data.count(int) == 1:
            list_unique_int.append(int)
    for unique_int in list_unique_int:
        data.remove(unique_int)
    return data
