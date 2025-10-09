import sys
input = sys.stdin.readline

N, M = map(int, input().split())

_set = set()

for _ in range(N):
    _set.add(input().rstrip())

for _ in range(M):
    sentence = input().rstrip().split(",")
    for word in sentence:
        if word in _set:
            _set.remove(word)

    print(len(_set))
