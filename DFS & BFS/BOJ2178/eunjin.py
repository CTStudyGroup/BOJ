# 입력 받기

# # dfs 하다가 망한 풀이
# N, M = map(int, input().split())
# adj_list = [[] for _ in range(N+2)]
# adj_list[0] = [0]*(M+2)
# adj_list[N+1] = [0]*(M+2)

# for i in range(1, N+1):
#     adj_list[i] = [0]
#     string = input()
#     for x in range(M):
#         adj_list[i].append(int(string[x]))
#     adj_list[i].append(0)

# # for row in adj_list:
# #     for col in row:
# #         print(col, end=" ")
# #     print()

# visited = [[False]*(M+2) for _ in range(N+2)]

# cnt = 0
# cnt_list = []


# def get_next_node(r, c):
#     result = []
#     if(adj_list[r-1][c] and not visited[r-1][c]):
#         result.append([r-1, c])
#     if(adj_list[r][c-1] and not visited[r][c-1]):
#         result.append([r, c-1])
#     if(adj_list[r+1][c] and not visited[r+1][c]):
#         result.append([r+1, c])
#     if(adj_list[r][c+1] and not visited[r][c+1]):
#         result.append([r, c+1])
#     return result


# def dfs(r, c):
#     global cnt, adj_list, visited
#     if visited[r][c]:
#         return
#     if(r == N and c == M):
#         cnt_list.append(cnt+1)

#     visited[r][c] = True
#     cnt += 1

#     for next_node in get_next_node(r, c):
#         #print("next_node:", next_node)
#         dfs(next_node[0], next_node[1])
#         visited[next_node[0]][next_node[1]] = False
#         cnt -= 1


# dfs(1, 1)
# print(min(cnt_list))


# 가중치가 없는 그래프에서 최단 거리 구하기 = bfs

from collections import deque

# 2차원 배열에서 인접한 4칸 접근 방법
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
matrix = ['0'*(M+1)] + ['0' + input() for _ in range(N)]

# bfs로 탐색
q = deque()
visited = [[False]*(M+1) for _ in range(N+1)]

q.append((1, 1, 1))  # (dist, y, x) dist: 시작 노드로부터 현재 노드까지의 거리
visited[1][1] = True

while q:
    dist, y, x = q.popleft()

    if y == N and x == M:
        print(dist)
        exit()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 유효한 좌표 내에 있고, 아직 방문하지 않았고, 값이 1인 노드만 방문
        if(1 <= ny <= N and 1 <= nx <= M) and (not visited[ny][nx]) and (matrix[ny][nx] == '1'):
            q.append((dist+1, ny, nx))
            visited[ny][nx] = True

# 종점에 도달할 수 없는 경우
print(-1)
