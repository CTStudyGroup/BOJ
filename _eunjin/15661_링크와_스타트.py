import sys
from itertools import product

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 완전탐색
# 가능한 모든 링크/스타트팀 조합 생성성
comb = list(product([0, 1], repeat=N))
answer = sys.maxsize

for arr in comb:
    link = []  # 1인 애들
    start = []  # 0인 애들
    for i in range(N):
        if arr[i]:
            link.append(i)
        else:
            start.append(i)
    if len(link) < 2 or len(start) < 2:  # 팀 당 최소 2명 있어야 함
        continue

    lScore = 0
    sScore = 0

    # 링크팀 능력치
    for i in range(len(link)):
        for k in range(len(link)):
            if i == k:
                continue
            lScore += matrix[link[i]][link[k]]

    # 스타트팀 능력치
    for i in range(len(start)):
        for k in range(len(start)):
            if i == k:
                continue
            sScore += matrix[start[i]][start[k]]

    answer = min(answer, abs(lScore - sScore))

print(answer)

