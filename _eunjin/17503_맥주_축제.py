import sys
import heapq
input = sys.stdin.readline

# 도수 레벨 2^31까지 가능
# 범위 너무 커서 dp 같은 거 아님
# 이분탐색이나.. 그리디나 뭔가 다른 것
N, M, K = map(int, input().split())
beer = []
for _ in range(K):
    v, c = map(int, input().split())
    beer.append((v, c))

beer.sort(key=lambda x: x[1])

pick = []  # 현재 고른 맥주 우선순위 큐
pref = 0

for b in beer:
    heapq.heappush(pick, b)  # 현재 맥주 고르기
    pref += b[0]

    if len(pick) >= N:  # 전체 고른 맥주가 N개가 되면
        if pref >= M:  # 원하는 선호도 달성한 경우
            print(b[1])
            exit()
        else:  # 맥주를 N개 골랐는데 선호도가 모자란 경우
            pref -= heapq.heappop(pick)[0]

print(-1)
