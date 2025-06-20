import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

# 다익스트라
# 다음 노드가 흰 칸이면 비용 0
# 다음 노드가 검은 칸이면 비용 1
# 최단 경로 찾기

# for row in matrix:
#     for elem in row:
#         print(elem, end=" ")
#     print()

dist = [[INF] * N for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def dijkstra():
    q = []
    dist[0][0] = 0  # 시작 노드
    heapq.heappush(q, (0, 0, 0))  # d,y,x
    while q:
        curr_dist, cy, cx = heapq.heappop(q)

        if dist[cy][cx] < curr_dist:  # 최단 경로 아님
            continue

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            temp_dist = curr_dist

            if matrix[ny][nx] == "0":
                temp_dist += 1

            if temp_dist < dist[ny][nx]:  # 이 경로가 최단 경로이면
                dist[ny][nx] = temp_dist
                heapq.heappush(q, (temp_dist, ny, nx))


dijkstra()
print(dist[N - 1][N - 1])
