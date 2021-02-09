while True:
    data = sorted(list(map(int, input().split())))
    if not data[0]:
        break
    
    result = (data[0]**2 + data[1]**2 == data[2]**2)
    if result:
        print('right')
    else:
        print('wrong')