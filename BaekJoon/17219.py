import sys

N, M = map(int, input().split())

url_password = {}
for _ in range(N):
    url, password = sys.stdin.readline().rstrip().split()
    url_password[url] = password

for _ in range(M):
    url = sys.stdin.readline().rstrip()
    print(url_password[url])