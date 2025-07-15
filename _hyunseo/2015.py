import sys
from collections import defaultdict
input = sys.stdin.readline
dic = defaultdict(int)

N, K = map(int, input().split())
arr = (list(map(int, input().split())))

dp = []
part_sum = 0
answer = 0

dic[0] = 1

for a in arr:
    part_sum += a
    answer += dic[part_sum - K]
    dic[part_sum] += 1

print(answer)
