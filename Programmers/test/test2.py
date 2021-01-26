def solution(arr1, arr2):
    count = 0
    for str1 in arr1:
        open = 0
        close = 0
        for s1 in str1:
            if s1 == '(':
                open += 1
            else:
                close += 1
            if close > open:
                break
        else:
            for str2 in arr2:
                open_ = open
                close_ = close
                for s2 in str2:
                    if s2 == '(':
                        open_ += 1
                    else:
                        close_ += 1
                    if close_ > open_:
                        break
                else:
                    if open_ == close_:
                        count += 1

    return count

print(solution(["()", "(()", "(", "(())"],	[")()","()", "(())", ")()"]))
