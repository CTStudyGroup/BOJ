import sys
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 같은 원소 K개 이하인 LCS 길이
answer = 0
_dict = defaultdict(int)
left, right = 0, 0

while right < N:
    # print(_dict)
    if _dict[arr[right]] >= K:
        while _dict[arr[right]] >= K:
            _dict[arr[left]] -= 1
            left += 1
    _dict[arr[right]] += 1
    right += 1
    # print(right, left)
    answer = max(answer, right - left)

print(answer)
