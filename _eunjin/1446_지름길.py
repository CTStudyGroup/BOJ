from itertools import product

N, D = map(int, input().split())
roads = []
for _ in range(N):
    s, e, l = map(int, input().split())
    roads.append((s, e, l))

roads.sort(key=lambda x: x[0])

answer = 10001
for use in product([0, 1], repeat=N):
    curr = 0
    dist = 0
    for i in range(len(use)):
        if use[i]:
            start = roads[i][0]
            end = roads[i][1]
            length = roads[i][2]

            if curr > start:
                continue
            if end > D:
                continue

            dist += start - curr  # 기존 위치 ~ 지름길 시작점까지는 그냥 이동

            # 지름길 이동
            dist += length
            curr = end
    dist += D - curr  # 남은 거리 그냥 이동
    answer = min(answer, dist)

print(answer)
