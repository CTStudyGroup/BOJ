import heapq
import sys
input = sys.stdin.readline

# 그냥 다익스트라
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
INF = sys.maxsize

def dijkstra():
    q = []
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = matrix[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))  # (dist,y,x)

    while q:
        cd, cy, cx = heapq.heappop(q)

        if cy == N - 1 and cx == N - 1:
            return cd

        if dist[cy][cx] < cd:
            continue

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                td = cd + matrix[ny][nx]
                if td < dist[ny][nx]:  # 거리가 더 짧을 때에만 탐색
                    dist[ny][nx] = td
                    heapq.heappush(q, (td, ny, nx))


t = 1
while True:
    N = int(input().strip())
    if N == 0:
        exit()

    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = dijkstra()
    print(f"Problem {t}: {answer}")
    t += 1
