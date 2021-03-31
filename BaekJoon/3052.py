inputData = [int(input()) for x in range(10)]
reminder = list(map(lambda x: x%42, inputData))
print(len(set(reminder)))
