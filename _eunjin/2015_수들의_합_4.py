import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 완전탐색 불가
_dict = {}
_dict[0] = 1

p_sum = 0
answer = 0

for a in A:
    p_sum += a

    if p_sum - K in _dict:
        answer += _dict[p_sum - K]

    if p_sum in _dict:
        _dict[p_sum] = _dict[p_sum] + 1
    else:
        _dict[p_sum] = 1

print(answer)
