import heapq

n = int(input())

hq = []
max_day = 0
for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(hq, (-w, d))
    if max_day < d:
        max_day = d

assigned = [False] * (max_day + 1)

score = 0
while hq:
    # 가장 스코어 높은 순으로 가져와서
    w, d = heapq.heappop(hq)
    w = -w

    # d일부터 1일 까지 거꾸로 돌면서 비어있는 날 중에 최대한 늦게 배정
    for i in range(d, 0, -1):
        if assigned[i]:
            continue

        assigned[i] = True
        score += w
        break

print(score)