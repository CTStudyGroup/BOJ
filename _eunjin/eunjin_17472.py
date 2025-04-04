from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy1 = [1, 0, -1, 0]
dx1 = [0, -1, 0, 1]

# 섬 좌표 딕셔너리 구하기
island_dict = {}
visited = [[False] * M for _ in range(N)]
k = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            island_dict[k] = []

            while q:
                y, x = q.popleft()
                island_dict[k].append((y, x))

                for z in range(4):
                    ny = y + dy1[z]
                    nx = x + dx1[z]

                    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
            k += 1


# 섬 matrix 구하기
island_idx = island_dict.keys()
I = len(island_idx)
island_matrix = [[-1] * M for _ in range(N)]
for key, values in island_dict.items():
    for y, x in values:
        island_matrix[y][x] = key

# 다리 방향은 가로 or 세로, 길이가 2 이상이어야 함
def get_row_bridges(y, x):
    ret = []  # [연결된 섬 인덱스, 거리]의 리스트
    # 왼쪽 방향
    nx = x - 1
    dist = 0
    while nx >= 0:
        if matrix[y][nx] == 1:
            if island_matrix[y][nx] != island_matrix[y][x] and dist != 1:  # 다음 땅이 같은 섬의 땅이 아닌 경우에만
                ret.append([island_matrix[y][nx], dist])
            break
        else:
            nx -= 1
            dist += 1

    # 오른쪽 방향
    nx = x + 1
    dist = 0
    while nx < M:
        if matrix[y][nx] == 1:
            if island_matrix[y][nx] != island_matrix[y][x] and dist != 1:
                ret.append([island_matrix[y][nx], dist])
            break
        else:
            nx += 1
            dist += 1

    return ret

def get_col_bridges(y, x):
    ret = []  # [연결된 섬 인덱스, 거리]의 리스트
    # 위쪽 방향
    ny = y - 1
    dist = 0
    while ny >= 0:
        if matrix[ny][x] == 1:
            if island_matrix[ny][x] != island_matrix[y][x] and dist != 1:  # 다음 땅이 같은 섬의 땅이 아닌 경우에만
                ret.append([island_matrix[ny][x], dist])
            break
        else:
            ny -= 1
            dist += 1

    # 아래쪽 방향
    ny = y + 1
    dist = 0
    while ny < N:
        if matrix[ny][x] == 1:
            if island_matrix[ny][x] != island_matrix[y][x] and dist != 1:
                ret.append([island_matrix[ny][x], dist])
            break
        else:
            ny += 1
            dist += 1

    return ret


# 다리는 섬의 개수-1개 있으면 모든 섬 연결 가능
# 각 섬 -> 다른섬으로 가는 거리를 모두 계산해서 가중치 있는 인접리스트 형식으로 저장
# 그 인접리스트 탐색하면서 최솟값 되는 경로 찾기

# 그냥 각 섬의 모든 땅마다 가로, 세로로 뻗어 나가면서 다른 섬을 만나는지를 확인해서 그걸 두 섬을 연결하는 다리 길이로 보는게 낫겠다

# adj_list[a][b]: a->b로 가는 모든 다리의 길이 리스트
adj_list = [[[] for _ in range(I)] for _ in range(I)]

# start->end로 가는 모든 다리 길이 구해서 adj_list[start][end]에 저장
for start in island_idx:  # 모든 섬마다
    for land in island_dict[start]:  # 해당 섬의 모든 땅 좌표마다
        row = get_row_bridges(land[0], land[1])
        col = get_col_bridges(land[0], land[1])
        # print("=====land:", land[0], ",", land[1], ", island:", island_matrix[land[0]][land[1]], " ============")
        # print("row:", row)
        # print("col:", col)
        bridges = row + col
        for bridge in bridges:
            adj_list[start][bridge[0]].append(bridge[1])  # start -> end로 가는 다리 길이 저장

# min_adj_list[a][b]: a->b로 가는 다리 길이 최솟값
min_adj_list = [[0] * I for _ in range(I)]
for i in range(I):
    for j in range(I):
        if adj_list[i][j]:
            min_adj_list[i][j] = min(adj_list[i][j])

# 최소 신장 트리 구하기
# 1. 간선 리스트 생성
edges = []
for i in range(I):
    for j in range(i + 1, I):
        cost = min_adj_list[i][j]
        if cost > 0:
            edges.append((cost, i, j))  # (비용, 노드1, 노드2)

# 2. 유니온 파인드 함수 정의
parent = [i for i in range(I)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return False
    parent[v_root] = u_root
    return True

# 3. 크루스칼 알고리즘 수행
edges.sort()
total_cost = 0
connected_edges = 0

for cost, u, v in edges:
    if union(u, v):
        total_cost += cost
        connected_edges += 1

# 4. 결과 출력
if connected_edges == I - 1:
    print(total_cost)
else:
    print(-1)  # 모든 섬을 연결할 수 없는 경우
