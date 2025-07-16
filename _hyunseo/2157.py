import sys
from collections import defaultdict

input = sys.stdin.readline

# 총 도시 개수 <= 300
# 지나야 하는 최대 도시 개수 <= N
# 개설된 항공로 수, <= 100,000
N, M, K = map(int, input().split())

# [0] 에서 [1]로 가는 항공편, 기내식 점수 : [c]
dic = defaultdict(list)
for _ in range(K) :
    a, b, c = map(int, input().split())
    if a < b :
        dic[a].append((b,c))
dp = [[-float('inf')] * (M + 1) for _ in range(N + 1)]
dp[1][1] = 0

for city in range(1, N + 1):
    for cnt in range(1, M):
        if dp[city][cnt] == -float('inf'):
            continue
        for next_city, food in dic[city]:
            if cnt + 1 <= M:
                if dp[next_city][cnt + 1] < dp[city][cnt] + food:
                    dp[next_city][cnt + 1] = dp[city][cnt] + food

# N번 도시에 도착한 값들 중 최대
answer = max(dp[N][2:M+1], default=0)
print(answer)
'''메모리 제한 알아보기...... '''
'''answer 전역 변수 이런거 알아보기. '''
