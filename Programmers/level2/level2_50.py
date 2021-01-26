# [3차] 파일명 정렬
import re

def solution(files):
    files_ = []
    for file in files:
        p = re.compile('(^\D+)(\d+)(.*)')
        m = p.match(file)
        files_.append([m.group(1), m.group(2), m.group(3)])
    files_.sort(key=lambda x: int(x[1]))
    files_.sort(key=lambda x: x[0].lower())
    return [''.join(file) for file in files_]

"""
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b
"""
