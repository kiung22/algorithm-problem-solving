def checkio(array):
    
    if array:
        return sum(array[::2]) * array[-1]
    else:
        return 0
