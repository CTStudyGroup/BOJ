import sys
input = sys.stdin.readline
N, M = map(int, input().split())

_set = set()
for _ in range(N):
    _set.add(input())

answer = 0
for _ in range(M):
    if input() in _set:
        answer += 1

print(answer)
