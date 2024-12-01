from itertools import combinations

# 입력 받기
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# print(matrix)
store = []
houses = []

for y in range(N):
    for x in range(N):
        if matrix[y][x] == 2:
            store.append((y, x))
        if matrix[y][x] == 1:
            houses.append((y, x))

# print("store:", store)
# print("houses:", houses)

chicken_dist = []
# 치킨집 선택 조합 생성
comb_list = list(combinations(store, M))
for i in range(len(comb_list)):
    chickens = comb_list[i]
    # print(chickens)
    total_dist = 0
    # 각 치킨집 조합에 따른 각 집에서의 치킨 거리 계산
    for j in range(len(houses)):
        house = houses[j]
        # print("house:", house)
        dist = 100
        for chicken in chickens:
            dist = min(dist, abs(chicken[0]-house[0])+abs(chicken[1]-house[1]))

        # 각 치킨 조합에 따른 치킨 거리 합 계산
        total_dist += dist
    chicken_dist.append(total_dist)

# 최솟값 출력
print(min(chicken_dist))
