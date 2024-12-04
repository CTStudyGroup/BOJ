import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
_dict = {}

for _ in range(N):
    key, value = input().split()
    _dict[key] = value

for _ in range(M):
    search = input().rstrip()
    print(_dict[search])
