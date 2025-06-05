from collections import defaultdict

N, M = map(int, input().split())
_dict = defaultdict(int)
for _ in range(N):
    st = input()
    _dict[st] += 1

for _ in range(M):
    words = list(input().split(','))

    for word in words:
        _dict[word] -= 1

    cnt = 0
    for n in _dict.values():
        if n > 0:
            cnt += n

    print(cnt)
