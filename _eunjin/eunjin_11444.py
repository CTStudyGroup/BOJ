import sys
sys.setrecursionlimit(10**8)

# 입력 받기
n = int(input())

_dict = {}
_dict[0] = 0
_dict[1] = 1
_dict[2] = 1


def dp(i):
    if i not in _dict:
        if i % 2 == 0:
            _dict[i] = (dp(i//2)*(dp(i//2) + 2*dp(i//2-1))) % 1000000007
        else:
            _dict[i] = (dp(i//2)**2 + dp(i//2+1)**2) % 1000000007
    return _dict[i]


print(dp(n))
