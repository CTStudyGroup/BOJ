from itertools import combinations

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def get_cost(y, x):  # (y,x) 좌표에 씨앗을 심은 경우의 비용
    global matrix
    ret = matrix[y][x]

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        ret += matrix[ny][nx]

    return ret


def isVisited(y, x):  # (y,x) 좌표에 꽃이 피어있는지 여부
    global visited
    if visited[y][x]:
        return True

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if visited[ny][nx]:
            return True

    return False


def visit(y, x):
    global visited
    visited[y][x] = True

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        visited[ny][nx] = True


flower_cnt = 0
total_cost = 0

while(flower_cnt < 3):
    min_cost = 1001
    min_y, min_x = -1, -1
    for y in range(1, N-1):
        for x in range(1, N-1):
            if isVisited(y, x):
                continue

            cost = get_cost(y, x)
            if cost < min_cost:
                min_y, min_x = y, x
                min_cost = cost

    visit(min_y, min_x)
    flower_cnt += 1
    total_cost += min_cost

print(total_cost)
print(visited)

# 좌표 3개 선택하는 모든 조합
coords = [(i, j) for i in range(1, N-1) for j in range(1, N-1)]
combs = list(combinations(coords, 3))

min_cost = 1001*3
for comb in combs:
    visited = [[False]*N for _ in range(N)]
    cost = 0
    valid = True

    for cord in comb:
        if isVisited(cord[0], cord[1]):
            valid = False
            break
        cost += get_cost(cord[0], cord[1])
        visit(cord[0], cord[1])

    if valid:
        min_cost = min(min_cost, cost)

print(min_cost)
