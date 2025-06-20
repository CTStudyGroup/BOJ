import heapq

def dijkstra(board, n):
    distance = [[float('inf')]*n for _ in range(n)]
    pq = [(0, 0, 0)]
    distance[0][0] = 0
    
    while pq:
        cost, x, y = heapq.heappop(pq)

        if cost>distance[x][y]: continue
        if (x, y) == (n-1, n-1):
            return cost
        
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                ncost = cost + abs(board[nx][ny] - 1)
                if ncost < distance[nx][ny]:
                    distance[nx][ny] = ncost
                    heapq.heappush(pq, (ncost, nx, ny))

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
print(dijkstra(board, n))