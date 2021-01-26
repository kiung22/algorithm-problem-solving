def checkio(str_number, radix):
    from string import ascii_uppercase
    
    dict_number = dict(zip(ascii_uppercase,range(10,36)))
    answer = 0
    n = 0
    for key in range(0,10):
        dict_number[str(key)] = key
    
    for i in str_number:
        if dict_number[i] < radix:
            answer += dict_number[i]*radix**(len(str_number)-1-n)
            n += 1
        else:
            return -1
    return answer

            
    
