# 오픈채팅방
def solution(record):
    record = [s.split() for s in record]
    user = {}
    for s in record:
        if len(s) < 3:
            continue
        user[s[1]] = s[2]

    answer = []
    for s in record:
        if s[0] == "Enter":
            answer.append(f"{user[s[1]]}님이 들어왔습니다.")
        elif s[0] == "Leave":
            answer.append(f"{user[s[1]]}님이 나갔습니다.")

    return answer
