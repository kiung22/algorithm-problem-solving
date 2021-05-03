import re

def solution(new_id):
    # 1단계
    new_id_1 = new_id.lower()

    # 2단계
    new_id_2 = re.sub('[^a-z0-9\-_.]', '', new_id_1)

    # 3단계
    new_id_3 = re.sub('\.+', '.', new_id_2)

    # 4단계
    new_id_4 = new_id_3.strip('.')

    # 5단계
    if not new_id_4:
        new_id_5 = 'a'
    else:
        new_id_5 = new_id_4
    
    # 6단계
    if len(new_id_5) >= 16:
        new_id_6 = new_id_5[:15].rstrip('.')
    else:
        new_id_6 = new_id_5
    
    # 7단계
    new_id_7 = new_id_6
    while len(new_id_7) <= 2:
        new_id_7 += new_id_7[-1]

    return new_id_7

print(solution('...!@BaT#*.....y.abcdefghijklm.'))