from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 망한 풀이
# # 안전영역의 크기
# zero = 0
# for row in matrix:
#     for col in row:
#         if(col == 0):
#             zero += 1


# def dfs(y, x):
#     global matrix, visited, dy, dx, cnt

#     if(visited[y][x]):
#         return

#     visited[y][x] = True
#     cnt -= 1

#     for i in range(4):
#         ny = y+dy[i]
#         nx = x + dx[i]
#         if(0 <= ny < N and 0 <= nx < M) and (matrix[ny][nx] == 0):
#             dfs(ny, nx)


# # 빈칸 좌표에 대해 가능한 모든 벽의 조합 탐색
# # 벽 후보 리스트 생성
# cord = []
# for y in range(N):
#     for x in range(M):
#         if(matrix[y][x] == 0):
#             cord.append([y, x])


# # 가능한 모든 벽 조합 리스트
# wall_comb = list(combinations(cord, 3))

# # 최대 안전 영역의 크기
# max_zero = 0

# for walls in wall_comb:
#     # 벽 설치
#     for wall in walls:
#         matrix[wall[0]][wall[1]] = 1

#     print(matrix)
#     # 바이러스 전파
#     visited = [[False]*M for _ in range(N)]
#     cnt = zero
#     for y in range(N):
#         for x in range(M):
#             if(matrix[y][x] == 2):
#                 dfs(y, x)

#     print("walls:", walls, ", cnt:", cnt)
#     max_zero = max(max_zero, cnt)

#     # 벽 설치 해제
#     for wall in walls:
#         matrix[wall[0]][wall[1]] = 0

# print(max_zero)

def bfs(graph):
    q = deque()
    # 바이러스 위치 queue에 추가
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 2:
                q.append((y, x))

    while q:
        node = q.popleft()
        for i in range(4):
            ny = node[0]+dy[i]
            nx = node[1]+dx[i]

            # 유효한 좌표이면서 아직 방문하지 않은 안전 영역인 경우
            if(0 <= ny < N and 0 <= nx < M) and graph[ny][nx] == 0:
                graph[ny][nx] = 2  # 바이러스 감염
                q.append((ny, nx))

    global result
    cnt = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 0:
                cnt += 1

    # 안전영역 최대 크기 업데이트
    result = max(result, cnt)


result = 0

# 빈칸 좌표에 대해 가능한 모든 벽의 조합 탐색
# 벽 후보 리스트 생성
cord = []
for y in range(N):
    for x in range(M):
        if(matrix[y][x] == 0):
            cord.append([y, x])


# 가능한 모든 벽 조합 리스트
for c in combinations(cord, 3):
    graph = copy.deepcopy(matrix)
    for y, x in c:
        graph[y][x] = 1  # 벽 설치
    bfs(graph)


print(result)
