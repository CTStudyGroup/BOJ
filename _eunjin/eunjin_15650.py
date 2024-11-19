from itertools import combinations

# 입력 받기
N, M = map(int, input().split())

arr = list(combinations(range(1, N+1), M))

for elem in arr:
    print(' '.join(map(str, elem)))
