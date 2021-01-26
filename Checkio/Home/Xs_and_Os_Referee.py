def checkio(game_result):
    result = ''.join(game_result)
    result_list = []
    result_list.extend(result[::4], result[2:8:2])
    for i in range(3):
        result_list.extend([game_result[i],
                            result[i::3])

    if "XXX" in result_list and "OOO" not in result_list:
        return "X"
    elif "OOO" in result_list and "XXX" not in result_list:
        return "O"
    else:
        return "D"
