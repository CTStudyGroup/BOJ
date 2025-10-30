import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 특정 덩어리 구매하는 경우 그보다 싼 고기는 비용 없이 얻을 수 있음
# 원하는 양만 구매
# 가격이 싸면 필요한 양보다 더 많이 살수도 있음
# 원하는 양만큼 구매하기 위해 필요한 최소 비용

# 어차피 하나 구매하면 그보다 싼 애들은 다 얻는거라서
# 누적합인가??

arr.sort(key=lambda x: (x[1], -x[0]))

curr_p = 0
before_p = -1
curr_w = 0
answer = int(1e12)
for w, p in arr:
    if p > before_p:
        before_p = p
        curr_p = p
    else:
        curr_p += p
    curr_w += w
    if curr_w >= M:
        answer = min(answer, curr_p)

if answer == int(1e12):
    print(-1)
else:
    print(answer)
