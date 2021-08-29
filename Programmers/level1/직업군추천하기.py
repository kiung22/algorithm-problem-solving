def solution(table, languages, preference):
    table_dict = {}
    for column in table:
        column = column.split()
        table_dict[column[0]] = {}
        score = 5
        for language in column[1:]:
            table_dict[column[0]][language] = score
            score -= 1
    
    answer = ''
    max_score = 0
    N = len(languages)
    for key, value in table_dict.items():
        score = 0
        for lang, pref in zip(languages, preference):
            score += value.get(lang, 0) * pref

        if score > max_score:
            max_score = score
            answer = key
        elif score == max_score and key < answer:
            answer = key

    return answer

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))